import os
import tree_sitter_cpp as stcpp
from tree_sitter import Language, Parser, Query, QueryCursor
from typing import cast
from anson.io.odysz.anson import Anson
from semanticshare.gen.cmake import CSettings

from qury_strings import fieldeclpointer_funcdecl_fdretdecl, field_id_isfunc


def parse_anson(config: CSettings, namespace="anson"):
    src_files = config.headers if hasattr(config, 'headers') else []
    output_filename = config.json_h if hasattr(config, 'json_h') else "json.hpp"

    CPP_LANGUAGE = Language(stcpp.language())
    parser = Parser(CPP_LANGUAGE)

    # In tree-sitter 0.25.2, Query needs language and string
    query_string = field_id_isfunc

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
                base = caps['base_name'][0].text.decode('utf8') if 'base_name' in caps else None

                # handle class
                # IGNORE TYPED CLASSES: Check if parent is template_declaration
                is_template = False
                p = class_node.parent
                while p and p != 'class_specifier':
                    if p.type == "template_declaration":
                        is_template = True
                        break
                    if p.type in ["translation_unit", "declaration_list"]: break
                    p = p.parent
                if is_template: continue

                if cname not in found_classes:
                    found_classes[cname] = {"base": base, "fields": []}
                if base == "AnsonBody" and cname not in anson_body_subclasses:
                    anson_body_subclasses.append((cname, base))

                if "field_decl" in caps:
                    is_static = False
                    if "storage" in caps:
                        for s_node in caps["storage"]:
                            if s_node.text.decode('utf8') == "static":
                                is_static = True
                                break
                    if is_static:
                        print(cname, "S", caps["field_decl"][0].text.decode('utf8'))
                        continue

                    # e.g. ['Anson']['fields']: (string, type)
                    found_classes[cname]['fields'].append((caps["field_type"][0].text.decode('utf8'),
                                                           caps["field_decl"][0].text.decode('utf8')))
                    print(cname, "Memb", caps["field_type"][0].text.decode('utf8'),
                                         caps["field_decl"][0].text.decode('utf8'))

                elif "ctor_name" in caps:
                    ctor_name = caps["ctor_name"][0].text.decode('utf8')

                    if 'ctors' not in found_classes[cname]:
                        found_classes[cname]['ctors'] = []

                    if ctor_name == cname:
                        params_node = caps["ctor_params"][0]

                        # Iterate through the children of the parameter_list
                        type_list = []
                        for param in params_node.children:
                            if param.type == "parameter_declaration":
                                # e.g., 'int', 'std::string', 'AnsonBody'
                                type_node = param.child_by_field_name("type")
                                if not type_node: continue

                                full_type_str = type_node.text.decode('utf8')
                                # Check the declarator for pointers/references but ignore the identifier
                                decl_node = param.child_by_field_name("declarator")
                                if decl_node:
                                    curr = decl_node
                                    # Peel back layers to find symbols like * or & while ignoring the name
                                    while curr:
                                        if curr.type in ["pointer_declarator", "reference_declarator"]:
                                            # Find the symbol (* or &) among children
                                            for child in curr.children:
                                                if child.type in ["*", "&", "&&"]:
                                                    full_type_str += child.text.decode('utf8')
                                            curr = curr.child_by_field_name("declarator")
                                        else:
                                            # We reached the identifier (the name), so we stop
                                            break

                                type_list.append(full_type_str.strip())
                        found_classes[cname]['ctors'].append(type_list)
                        print(cname, 'Ctor', ctor_name, type_list)
                    else:
                        print(cname, 'Func', ctor_name)
    return found_enums, found_classes

def gen_entt_registry(founds, settings: CSettings, namespace='anson'):
    found_enums, found_classes = founds
    # 3. Generate Output
    indent = "    "
    output = ['#pragma once',
              '',
              '#include <entt/meta/factory.hpp>',
              '#include <entt/meta/meta.hpp>',
              '',
              'using namespace entt::literals;',
              '']

    for s in settings.src:
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
        output.append(f"{indent * 2}.type(\"{cname}\"_hs)")

        if 'ctors' in info:
            for params in info["ctors"]:
                output.append(f"{indent * 2}.ctor{params}()")

        if info["base"]:
            output.append(f"{indent * 2}.base<{namespace}::{info['base']}>()")
        for ftype, fname in info["fields"]:
            output.append(f"{indent * 2}.data<&{namespace}::{cname}::{fname}>(\"{fname}\"_hs, \"{fname}\")")
        output.append(f"{indent * 2};\n")

    # # Specialized AnsonMsg Template Registration
    # for sub, base in anson_body_subclasses:
    #     output.append(f"{indent}// Specialized AnsonMsg for {sub}")
    #     output.append(f"{indent}entt::meta_factory<{namespace}::AnsonMsg<{namespace}::{sub}>>()")
    #     output.append(f"{indent * 2}.type(\"AnsonMsg{sub}\"_hs)")
    #     output.append(f"{indent * 2}.base<{namespace}::{base}>()")
    #
    #     # TODO FIXME LLM Error
    #     output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::port>(\"port\"_hs, \"port\")")
    #     output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::body>(\"body\"_hs, \"body\");\n")

    output.append("}\n}")

    with open(settings.json_h, "w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    settings: CSettings = cast(CSettings, Anson.from_file("anson.json"))
    parse_anson(settings)