import os
import tree_sitter_cpp as stcpp
from tree_sitter import Language, Parser, Query, QueryCursor
from typing import cast
from anson.io.odysz.anson import Anson
from semanticshare.gen.cmake import CSettings


def generate_entt_registration(config: CSettings, namespace="anson"):
    src_files = config.headers if hasattr(config, 'headers') else []
    output_filename = config.json_h if hasattr(config, 'json_h') else "json.hpp"

    CPP_LANGUAGE = Language(stcpp.language())
    parser = Parser(CPP_LANGUAGE)

    # In tree-sitter 0.25.2, Query needs language and string
    query_string = """
        (enum_specifier 
            name: (type_identifier) @enum_name
            body: (enumerator_list (enumerator name: (identifier) @enum_val)))

        (class_specifier
            name: (type_identifier) @class_name
            (base_class_clause (type_identifier) @base_name)?
            body: (field_declaration_list 
                [
                    ;; Capture member variables and their storage specifiers
                    (field_declaration 
                        (storage_class_specifier)* @storage
                        type: (type_identifier) @field_type
                        declarator: (field_identifier) @field_name)
                    
                    ;; Capture constructors
                    (declaration
                        declarator: (function_declarator
                            declarator: (identifier) @ctor_name
                            parameters: (parameter_list) @ctor_params))
                ]
            ))
    """
    # This is not expected tree structure, deprecate and use gen-register-6.py, for travel AST tree, class wisely.
    query = Query(CPP_LANGUAGE, query_string)
    cursor = QueryCursor(query)

    found_enums = {}
    found_classes = {}
    anson_body_subclasses = []

    for header in src_files:
        if not os.path.exists(header): continue
        with open(header, "rb") as f:
            tree = parser.parse(f.read())

        # Use matches to maintain the relationship between names and their children
        # Ody: Gemini missed my fixation
        # matches = cursor.matches(query, tree.root_node)
        matches = cursor.matches(tree.root_node)

        for match in matches:
            # Ody: Gemini accepted my fixation
            # In version 0.25.2, match[1] is the captures dictionary
            caps = match[1]

            # 1. Capture Enums (Requirement for Port and MsgCode)
            if "enum_name" in caps:
                ename = caps["enum_name"][0].text.decode('utf8')
                if ename not in found_enums:
                    found_enums[ename] = []
                if "enum_val" in caps:
                    for v_node in caps["enum_val"]:
                        val_text = v_node.text.decode('utf8')
                        if val_text not in found_enums[ename]:
                            found_enums[ename].append(val_text)

            # 2. Capture Classes and Data Fields
            if "class_name" in caps:
                class_node = caps["class_name"][0]
                cname = class_node.text.decode('utf8')
                base = cname if "base_name" in caps else None

                # IGNORE TYPED CLASSES: Check if parent is template_declaration
                is_template = False
                p = class_node.parent
                while p:
                    if p.type == "template_declaration":
                        is_template = True
                        break
                    if p.type in ["translation_unit", "declaration_list"]: break
                    p = p.parent
                if is_template: continue

                # Check if the 'static' storage specifier exists for this field
                is_static = False
                if "storage" in caps:
                    for s_node in caps["storage"]:
                        if s_node.text.decode('utf8') == "static":
                            is_static = True
                            break

                if cname not in found_classes:
                    found_classes[cname] = {"base": base, "fields": []}

                if "field_name" in caps and not is_static:
                    fname = caps["field_name"][0].text.decode('utf8')
                    if fname not in [f[1] for f in found_classes[cname]["fields"]]:
                        found_classes[cname]["fields"].append((None, fname))

                # Track AnsonBody subclasses for Template registration
                if base == "AnsonBody" and cname not in anson_body_subclasses:
                    anson_body_subclasses.append(cname)

    # 3. Generate Output
    indent = "    "
    output = ["#pragma once", '',
              '#include <entt/meta/factory.hpp>',
              '#include <entt/meta/meta.hpp>', '',
              f'using namespace entt::literals;', '']

    for s in src_files:
        output.append(f'#include "{os.path.basename(s)}"')

    output.append(f"\nnamespace {namespace} {{")
    output.append(f"inline void register_meta() {{")

    # Enum Registration (Ensures Port and MsgCode are registered)
    for ename, evals in found_enums.items():
        output.append(f"{indent}// Register {ename} enum")
        output.append(f"{indent}entt::meta_factory<{namespace}::{ename}>()")
        output.append(f"{indent * 2}.type(\"{ename}\"_hs)")
        for v in evals:
            output.append(f"{indent * 2}.data<{namespace}::{ename}::{v}>(\"{v}\"_hs, \"{v}\")")
        output.append(f"{indent * 2};\n")

    # Class Registration with Data Fields
    for cname, info in found_classes.items():
        if cname in found_enums: continue
        output.append(f"{indent}entt::meta_factory<{namespace}::{cname}>()")
        output.append(f"{indent * 2}.type(\"{cname}\"_hs).ctor<>()")
        if info["base"]:
            output.append(f"{indent * 2}.base<{namespace}::{info['base']}>()")
        for _, fname in info["fields"]:
            output.append(f"{indent * 2}.data<&{namespace}::{cname}::{fname}>(\"{fname}\"_hs, \"{fname}\")")
        output.append(f"{indent * 2};\n")

    # Specialized AnsonMsg Template Registration
    for sub in anson_body_subclasses:
        output.append(f"{indent}// Specialized AnsonMsg for {sub}")
        output.append(f"{indent}entt::meta_factory<{namespace}::AnsonMsg<{namespace}::{sub}>>()")
        output.append(f"{indent * 2}.type(\"AnsonMsg{sub}\"_hs)")
        output.append(f"{indent * 2}.base<{namespace}::Anson>()")
        output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::port>(\"port\"_hs, \"port\")")
        output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::body>(\"body\"_hs, \"body\");\n")

    output.append("}\n}")

    with open(output_filename, "w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    settings: CSettings = cast(CSettings, Anson.from_file("anson.json"))
    generate_entt_registration(settings)