'''
Prerequisite: Install pypi package anson.py3 and semantics.py3.
'''
from typing import cast

import CppHeaderParser
import sys
import os
from anson.io.odysz.anson import Anson
from semanticshare.gen.cmake import CSettings

'''
Gemini generated Anson class for the gen.json configuration.
============================================================

    from anson.anson import Anson
    #    anson.io.odysz.anson import Anson

    class CmakeSettings(Anson):
        """Mapping for io.oz.gen.cmake.settings"""
        def __init__(self):
            super().__init__()
            self.type = "io.oz.gen.cmake.settings" # not correct. Gemini doesn't know the type's rule. But shouldn't it can be fixed figured out?
            self.src = []
            self.gen = ""

    # IMPORTANT: Register the type so the parser knows which class to instantiate
    from anson.anson import AnsonProtocol # not correct.
    AnsonProtocol.register("io.oz.gen.cmake.settings", CmakeSettings)
    # ^ I don't have such code anymore. Where did Gemini found it?
    # Actually I think it's somewhere tried in order versions/ designs. 

'''

def generate_entt_registration(config: CSettings, namespace="anson"):
    # 2. Extract settings from the Anson object
    src_files = config.headers if hasattr(config, 'headers') else []
    output_filename = config.json_h if hasattr(config, 'json_h') else "json.hpp"

    all_classes = []

    # 3. Code Generation Header
    output = []
    for header in src_files:
        output.append(f'#include "{os.path.basename(header)}"')
    output.append('#include <entt/meta/factory.hpp>\n#include <entt/meta/meta.hpp>\n')
    output.append(f"namespace {namespace} {{")
    output.append("inline void register_meta() {")
    output.append("    using namespace entt::literals;\n")

    # 4. AST Parsing Loop
    for header in src_files:
        try:
            cpp_header = CppHeaderParser.CppHeader(header)
            for class_name, class_obj in cpp_header.classes.items():
                # Filter: Templates & Virtual/Abstract
                if "<" in class_name: continue
                if any(m.get("virtual") for scope in ["public", "protected"]
                       for m in class_obj["methods"][scope]):
                    continue

                # Start Factory
                output.append(f"    entt::meta_factory<{namespace}::{class_name}>()")
                output.append(f"        .type(\"{class_name}\"_hs)")

                # DYNAMIC CONSTRUCTOR ITERATION
                public_methods = class_obj["methods"]["public"]
                for method in public_methods:
                    if method["name"] == class_name:  # It's a constructor
                        params = method.get("parameters", [])
                        if not params:
                            output.append("        .ctor<>()")
                        else:
                            # Map each parameter type dynamically
                            param_types = [p["type"] for p in params]
                            output.append(f"        .ctor<{', '.join(param_types)}>()")

                # Bases
                for inherit in class_obj.get("inherits", []):
                    b = (inherit.get("class") or inherit.get("point")).split("::")[-1]
                    output.append(f"        .base<{namespace}::{b}>()")

                # Fields
                for p in class_obj["properties"]["public"]:
                    if not p.get("static"):
                        f = p["name"]
                        output.append(f"        .data<&{namespace}::{class_name}::{f}>(\"{f}\"_hs, \"{f}\")")

                output.append("    ;\n")
        except Exception as e:
            print(f"// Error parsing {header}: {e}", file=sys.stderr)
    output.append("}\n}")

    # 5. Save to the file defined in gen.json
    with open(output_filename, "w") as f:
        f.write("\n".join(output))
    print(f"Generated {output_filename} successfully.")

if __name__ == "__main__":
    settings: CSettings = cast(CSettings, Anson.from_file("anson.json"))
    generate_entt_registration(settings)