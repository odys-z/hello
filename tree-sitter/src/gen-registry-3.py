import re
import sys
import os
import CppHeaderParser
from typing import cast
from anson.io.odysz.anson import Anson
from semanticshare.gen.cmake import CSettings


def generate_entt_registration(config: CSettings, namespace="anson"):
    src_files = config.headers if hasattr(config, 'headers') else []
    output_filename = config.json_h if hasattr(config, 'json_h') else "json.hpp"

    # Global tables to merge artifacts across all files
    global_classes = {}
    global_enums = []  # CppHeaderParser stores enums as a list of dicts

    # 1. Merge all ASTs first
    for header in src_files:
        try:
            cpp_header = CppHeaderParser.CppHeader(header)
            global_classes.update(cpp_header.classes)
            global_enums.extend(cpp_header.enums)  # Collect enums globally
            for ns in cpp_header.namespaces:
                if "enums" in ns:
                    global_enums.extend(ns["enums"])
        except Exception as e:
            print(f"// Error parsing file {header}: {e}", file=sys.stderr)

    indent = "    "
    output = [
        "/**",
        " * The equivalent of gen.antlr.json + JSONAnsonListener",
        " */",
        "#pragma once",
        "",
        '#include <entt/meta/factory.hpp>',
        '#include <entt/meta/meta.hpp>',
        '']

    for s in src_files:
        output.append(f'#include "{os.path.basename(s)}"')
    else:
        output.append('')

    output.append(f"namespace {namespace} {{")
    output.append('')
    output.append("inline void register_meta() {")
    output.append(f"{indent}using namespace entt::literals;\n")

    template_specializations = set()
    available_class_names = list(global_classes.keys())

    # 2. Process Classes
    for class_name, class_obj in global_classes.items():
        try:
            if "<" in class_name: continue
            if any(m.get("virtual") for scope in ["public", "protected"]
                   for m in class_obj["methods"][scope]):
                continue

            # Template Detection Logic
            for base_candidate in available_class_names:
                pattern = re.compile(rf"{base_candidate}<\s*([^>]+)\s*>")
                for search_obj in global_classes.values():
                    for prop in search_obj["properties"]["public"]:
                        ptype = prop.get("type", "")
                        match = pattern.search(ptype)
                        if match:
                            inner_type = match.group(1).split("::")[-1].strip()
                            template_specializations.add((base_candidate, inner_type))

            # Factory Generation
            output.append(f"{indent}entt::meta_factory<{namespace}::{class_name}>()")
            output.append(f"{indent * 2}.type(\"{class_name}\"_hs)")

            public_methods = class_obj["methods"]["public"]
            hasctor = False
            for method in public_methods:
                if method["name"] == class_name:
                    hasctor = True
                    params = method.get("parameters", [])
                    param_types = [p["type"].replace("string", "std::string") for p in params]
                    output.append(f"{indent * 2}.ctor<{', '.join(param_types)}>()")
            else:
                if not hasctor:
                    output.append(f"{indent * 2}// Needing a default ctor: .ctor<>()")

            for inherit in class_obj.get("inherits", []):
                b = (inherit.get("class") or inherit.get("point")).split("::")[-1]
                output.append(f"{indent * 2}.base<{namespace}::{b}>()")

            for p in class_obj["properties"]["public"]:
                if not p.get("static"):
                    f = p["name"]
                    output.append(f"{indent * 2}.data<&{namespace}::{class_name}::{f}>(\"{f}\"_hs, \"{f}\")")
            output.append("    ;\n")
        except Exception as cls_e:
            print(f"// Error processing class {class_name}: {cls_e}", file=sys.stderr)

    # 3. Process Enums (Port, MsgCode, etc.)
    for enm in global_enums:
        try:
            enum_name = enm.get("name")
            if not enum_name: continue  # Skip anonymous enums

            output.append(f"{indent}// Register {enum_name} enum")
            output.append(f"{indent}entt::meta_factory<{namespace}::{enum_name}>()")
            output.append(f"{indent * 2}.type(\"{enum_name}\"_hs)")

            # Iterate through enum values to register them as data
            for val in enm.get("values", []):
                v_name = val["name"]
                output.append(f"{indent * 2}.data<{namespace}::{enum_name}::{v_name}>(\"{v_name}\"_hs, \"{v_name}\")")

            output.append("    ;\n")
        except Exception as enm_e:
            print(f"// Error processing enum {enm.get('name')}: {enm_e}", file=sys.stderr)

    # 4. Process Specialized Templates
    for base_tmpl, inner_type in template_specializations:
        try:
            output.append(f"    // Specialized: {base_tmpl}<{inner_type}>")
            output.append(f"    entt::meta_factory<{namespace}::{base_tmpl}<{namespace}::{inner_type}>>()")
            output.append(f"{indent * 2}.type(\"{base_tmpl}_{inner_type}\"_hs)")
            output.append(f"{indent * 2}.base<{namespace}::Anson>()")
            output.append(
                f"{indent * 2}.data<&{namespace}::{base_tmpl}<{namespace}::{inner_type}>::body>(\"body\"_hs, \"body\")")
            output.append(
                f"{indent * 2}.data<&{namespace}::{base_tmpl}<{namespace}::{inner_type}>::port>(\"port\"_hs, \"port\")")
            output.append("    ;\n")
        except Exception as tmpl_e:
            print(f"// Error generating specialization {base_tmpl}<{inner_type}>: {tmpl_e}", file=sys.stderr)

    output.append("}\n}")

    with open(output_filename, "w") as f:
        f.write("\n".join(output))
    print(f"Generated {output_filename} successfully.")


if __name__ == "__main__":
    settings: CSettings = cast(CSettings, Anson.from_file("anson.json"))
    generate_entt_registration(settings)