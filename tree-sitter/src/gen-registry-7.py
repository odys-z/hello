'''
After questioning the flat table of query result, finally reached here,
hierarchically traverse of the the AST.
'''
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

    # Anchor Query: Find the main containers only
    query_string = """
        (class_specifier 
            name: (type_identifier) @class_name
            body: (field_declaration_list) @class_body) @class_node

        (enum_specifier 
            name: (type_identifier) @enum_name
            body: (enumerator_list) @enum_body) @enum_node
    """
    query = Query(CPP_LANGUAGE, query_string)
    cursor = QueryCursor(query)

    found_enums = {}
    found_classes = {}
    anson_body_subclasses = []

    for header in src_files:
        if not os.path.exists(header): continue
        with open(header, "rb") as f:
            tree = parser.parse(f.read())

        for match in cursor.matches(tree.root_node):
            caps = match[1]

            # --- PROCESS ENUMS ---
            if "enum_node" in caps:
                ename = caps["enum_name"][0].text.decode('utf8')
                body = caps["enum_body"][0]
                found_enums[ename] = []
                # Traverse enum body for values
                for child in body.children:
                    if child.type == "enumerator":
                        val_node = child.child_by_field_name("name")
                        if val_node:
                            found_enums[ename].append(val_node.text.decode('utf8'))

            # --- PROCESS CLASSES (Tree Traversal Style) ---
            elif "class_node" in caps:
                class_spec = caps["class_node"][0]
                cname = caps["class_name"][0].text.decode('utf8')

                # 1. Ignore Typed Classes (Templates like AnsonMsg<T>)
                if class_spec.parent.type == "template_declaration":
                    continue

                # 2. Get Base Class
                base_name = None
                base_clause = class_spec.child_by_field_name("base_class_clause")
                if base_clause:
                    # Capture the identifier inside the clause
                    for c in base_clause.children:
                        if c.type == "type_identifier":
                            base_name = c.text.decode('utf8')

                found_classes[cname] = {"base": base_name, "fields": [], "ctors": []}

                # 3. Step inside the Class Body
                body_node = caps["class_body"][0]
                for member in body_node.children:

                    # A. Capture Non-Static Fields
                    if member.type == "field_declaration":
                        modifiers = [c.text.decode('utf8') for c in member.children
                                     if c.type == "storage_class_specifier"]

                        if "static" in modifiers:
                            continue  # Ignore static fields (even if inline is present)

                        decl = member.child_by_field_name("declarator")
                        """
                        Whith the query, this decl cannot deprive pointer_declarator for a function return type in a simple way.
                        Say: 
                        virtual ostream toblock(); <- decl.type = function_declaration
                        virtual ostream* toblock(); <- debug: decl.type = pointer declarator
                        virtual ostream& toblock(); <- ?
                        virtual ostream** toblock(); <- decl is a pointer of pointer?
                        """
                        if decl:
                            found_classes[cname]["fields"].append(decl.text.decode('utf8'))

                    # B. Capture Constructors
                    elif member.type == "declaration":
                        func = member.child_by_field_name("declarator")
                        if func and func.type == "function_declarator":
                            fn_id = func.child_by_field_name("declarator")
                            if fn_id and fn_id.text.decode('utf8') == cname:
                                params = func.child_by_field_name("parameters").text.decode('utf8')
                                found_classes[cname]["ctors"].append(params)

                # Track subclasses for Template Registration
                if base_name == "AnsonBody":
                    anson_body_subclasses.append(cname)

    # --- GENERATE OUTPUT ---
    indent = "    "
    output = ["#pragma once", '#include <entt/meta/factory.hpp>', '#include <entt/meta/meta.hpp>', '']
    for s in src_files:
        output.append(f'#include "{os.path.basename(s)}"')

    output.append(f"\nnamespace {namespace} {{")
    output.append(f"inline void register_meta() {{")
    output.append(f"{indent}using namespace entt::literals;\n")

    # 1. Enums (Port, MsgCode)
    for ename, evals in found_enums.items():
        output.append(f"{indent}entt::meta_factory<{namespace}::{ename}>()")
        output.append(f"{indent * 2}.type(\"{ename}\"_hs)")
        for v in evals:
            output.append(f"{indent * 2}.data<{namespace}::{ename}::{v}>(\"{v}\"_hs, \"{v}\")")
        output.append(f"{indent * 2};\n")

    # 2. Classes (Fields and Ctors)
    clss_lns = []
    for cname, info in found_classes.items():
        # line = f"{indent}entt::meta_factory<{namespace}::{cname}>()\n{indent * 2}.type(\"{cname}\"_hs)"
        clss_lns.append(f"{indent}entt::meta_factory<{namespace}::{cname}>()")
        clss_lns.append(f"{indent * 2}.type(\"{cname}\"_hs)")
        for params in info["ctors"]:
            clss_lns.append(f"{indent * 2}.ctor{params}()")
        if info["base"]:
            clss_lns.append(f"{indent * 2}.base<{namespace}::{info['base']}>()")
        for fname in info["fields"]:
            clss_lns.append(f"{indent * 2}.data<&{namespace}::{cname}::{fname}>(\"{fname}\"_hs, \"{fname}\")")
        clss_lns.append(f"{indent * 2};\n")

    # 3. AnsonMsg Specializations
    for sub in anson_body_subclasses:
        output.append(f"{indent}entt::meta_factory<{namespace}::AnsonMsg<{namespace}::{sub}>>()")
        output.append(f"{indent * 2}.type(\"AnsonMsg{sub}\"_hs).base<{namespace}::Anson>()")
        output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::port>(\"port\"_hs, \"port\")")
        output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::body>(\"body\"_hs, \"body\");\n")

    output.append("}\n}")
    with open(output_filename, "w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    settings: CSettings = cast(CSettings, Anson.from_file("anson.json"))
    generate_entt_registration(settings)