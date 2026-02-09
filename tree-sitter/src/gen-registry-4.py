import os
import tree_sitter_cpp as stcpp
from tree_sitter import Language, Parser, Query, QueryCursor
from typing import cast
from anson.io.odysz.anson import Anson
from semanticshare.gen.cmake import CSettings


def generate_entt_registration(config: CSettings, namespace="anson"):
    src_files = config.headers if hasattr(config, 'headers') else []
    output_filename = config.json_h if hasattr(config, 'json_h') else "json.hpp"

    # 1. Setup Parser for 0.25.2
    CPP_LANGUAGE = Language(stcpp.language())
    parser = Parser(CPP_LANGUAGE)

    # 2. Define the Query
    # Note: enum_specifier body contains enumerator_list
    query_string = """
        (enum_specifier 
            name: (type_identifier) @enum_name
            body: (enumerator_list (enumerator name: (identifier) @enum_val)))

        (class_specifier
            name: (type_identifier) @class_name
            body: (field_declaration_list (field_declaration) @field))
    """
    # 0.25.2: Query takes (Language, str)
    query = Query(CPP_LANGUAGE, query_string)

    found_enums = {}
    found_classes = []

    for header in src_files:
        if not os.path.exists(header): continue

        with open(header, "rb") as f:
            content = f.read()
            tree = parser.parse(content)

        cursor = QueryCursor(query)
        # 3. Capture Logic
        # Returns a dict in 0.25.2: { tag: [Node, Node, ...] }
        captures = cursor.captures(tree.root_node)

        # Extract Enum data
        if "enum_name" in captures:
            for idx, name_node in enumerate(captures["enum_name"]):
                ename = name_node.text.decode('utf8')
                # Map values associated with this enum's range
                # Simple logic for jprotocol.h: get all enum_vals
                if "enum_val" in captures:
                    found_enums[ename] = [v.text.decode('utf8') for v in captures["enum_val"]]

        # Extract Class names
        if "class_name" in captures:
            for node in captures["class_name"]:
                found_classes.append(node.text.decode('utf8'))

            for field in captures["field"]:
                print(field)

    # 4. Generate Output
    indent = "    "
    output = ["#pragma once", '#include <entt/meta/factory.hpp>', '#include <entt/meta/meta.hpp>', '']
    for s in src_files:
        output.append(f'#include "{os.path.basename(s)}"')

    output.append(f"\nnamespace {namespace} {{")
    output.append(f"inline void register_meta() {{")
    output.append(f"{indent}using namespace entt::literals;\n")

    # Enum Registration (Port, MsgCode)
    for ename, evals in found_enums.items():
        output.append(f"{indent}entt::meta_factory<{namespace}::{ename}>()")
        output.append(f"{indent * 2}.type(\"{ename}\"_hs)")
        for v in evals:
            output.append(f"{indent * 2}.data<{namespace}::{ename}::{v}>(\"{v}\"_hs, \"{v}\")")
        output.append(f"{indent * 2};")

    # Class Registration
    for cname in found_classes:
        if cname in found_enums: continue
        output.append(f"{indent}entt::meta_factory<{namespace}::{cname}>().type(\"{cname}\"_hs);")

    output.append("}\n}")

    with open(output_filename, "w") as f:
        f.write("\n".join(output))
    print(f"Generated {output_filename}")


if __name__ == "__main__":
    try:
        settings = cast(CSettings, Anson.from_file("anson.json"))
        generate_entt_registration(settings)
    except Exception as e:
        print(f"Error: {e}")