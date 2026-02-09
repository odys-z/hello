
import os
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, cast

import tree_sitter_cpp as stcpp
from tree_sitter import Language, Parser, Query, QueryCursor, Node

from anson.io.odysz.anson import Anson
from semanticshare.gen.cmake import CSettings
from query_strings import fieldecl_funcdecl_funcdef, field_id_isfunc


@dataclass
class MetaEnum(Anson):
    etype: str
    enums: List[str] = field(default_factory=list)

    def __init__(self, etype: str):
        super().__init__()
        self.etype = etype
        self.enums = []

@dataclass
class MetaClass(Anson):
    cname: str
    base: Optional[str] = None
    fields: List[Tuple[str, str]] = field(default_factory=list)  # (type, name)
    ctors: List[List[str]] = field(default_factory=list)  # list of arg types
    funcs: List[List[str]] = field(default_factory=list)  # list of arg types

    # Gemini lost the classical __init__(), resulting in error:
    # TypeError: MetaClass.__init__() missing 2 required positional arguments: 'verbose' and '__type__'
    def __init__(self, cname: str, base: str=None):
        super().__init__()
        self.cname = cname
        self.base = base
        self.fields = []
        self.ctors = []
        self.funcs = []
        # print(self.__type__, cname)


def extract_enum_data(caps: Dict[str, List[Node]], found_enums: Dict[str, MetaEnum]):
    """Extracts enum names and values into MetaEnum objects."""
    ename = caps["enum_name"][0].text.decode('utf8')
    if ename not in found_enums:
        found_enums[ename] = MetaEnum(etype=ename)

    if "enum_val" in caps:
        for v_node in caps["enum_val"]:
            val_text = v_node.text.decode('utf8')
            if val_text not in found_enums[ename].enums:
                found_enums[ename].enums.append(val_text)


def get_parameter_types(params_node: Node) -> List[str]:
    """Helper to extract pure types from a parameter list, ignoring variable names."""
    type_list = []
    for param in params_node.children:
        if param.type == "parameter_declaration":
            type_node = param.child_by_field_name("type")
            if not type_node: continue

            full_type = type_node.text.decode('utf8')
            decl_node = param.child_by_field_name("declarator")

            # Drill through pointers/references to get the full type string
            curr = decl_node
            while curr and curr.type in ["pointer_declarator", "reference_declarator"]:
                for child in curr.children:
                    if child.type in ["*", "&", "&&"]:
                        full_type += child.text.decode('utf8')
                curr = curr.child_by_field_name("declarator")

            type_list.append(full_type.strip())
    return type_list


def extract_class_member(caps: Dict[str, List[Node]], cname: str, meta: MetaClass):
    """Processes fields, methods, and constructors for a MetaClass."""
    # 1. Handle Fields (and filter out methods/static)
    if "field_decl" in caps:
        is_static = any(s.text.decode('utf8') == "static" for s in caps.get("storage", []))
        decl_node = caps["field_decl"][0]

        # Unwrap to check if it's a function prototype hidden in a field_declaration
        # curr = decl_node
        # while curr and curr.type in ["pointer_declarator", "reference_declarator"]:
        #     curr = curr.child_by_field_name("declarator")
        #
        # if curr.type == "function_declarator":
        #     # If it's a function/method, we handle ctor logic or skip regular methods
        #     fn_id = curr.child_by_field_name("declarator")
        #     params_node = curr.child_by_field_name("parameters")
        #     paras = get_parameter_types(params_node)
        #     if fn_id and fn_id.text.decode('utf8') == cname:
        #         meta.ctors.append(paras)
        #     else:
        #         f = [fn_id.text]
        #         f.extend(paras)
        #         # if not meta.funcs: meta.funcs = []
        #         meta.funcs.append(f)
        #
        #     return
        print('Field?', caps['field_name'][0].text.decode('utf8'),
                        caps['field_type'][0].text.decode('utf8'),
                        caps['field_register'][0].text.decode('utf8'))

        ftype = caps["field_type"][0].text.decode('utf8')
        if not is_static:
            meta.fields.append((ftype, decl_node.text.decode('utf8')))
        else:
            print("Ignore static", ftype, decl_node.text)

    # 2. Handle Explicit Constructors (from declaration or function_definition)
    elif "ctor_name" in caps:
        ctor_name = caps["ctor_name"][0].text.decode('utf8')
        if ctor_name == cname:
            params_node = caps["ctor_params"][0]
            meta.ctors.append(get_parameter_types(params_node))


def parse_anson(config: CSettings, namespace="anson"):
    src_files = config.headers if hasattr(config, 'headers') else []
    CPP_LANGUAGE = Language(stcpp.language())
    parser = Parser(CPP_LANGUAGE)
    query = Query(CPP_LANGUAGE, field_id_isfunc)
    cursor = QueryCursor(query)

    found_enums: Dict[str, MetaEnum] = {}
    found_classes: Dict[str, MetaClass] = {}

    for header in src_files:
        if not os.path.exists(header): continue
        with open(header, "rb") as f:
            tree = parser.parse(f.read())

        for match in cursor.matches(tree.root_node):
            caps = match[1]

            if "enum_name" in caps:
                extract_enum_data(caps, found_enums)

            if "class_name" in caps:
                class_node = caps["class_name"][0]
                cname = class_node.text.decode('utf8')

                # Filter templates
                is_template = False
                p = class_node.parent
                while p:
                    if p.type == "template_declaration":
                        is_template = True
                        break
                    if p.type in ["translation_unit", "field_declaration_list"]:
                        break
                    p = p.parent
                if is_template: continue

                if cname not in found_classes:
                    base = caps['base_name'][0].text.decode('utf8') if 'base_name' in caps else None
                    found_classes[cname] = MetaClass(cname=cname, base=base)

                extract_class_member(caps, cname, found_classes[cname])

    return found_enums, found_classes

if __name__ == "__main__":
    settings: CSettings = cast(CSettings, Anson.from_file("anson.json"))
    enums, classes = parse_anson(settings)
    for name, node in enums.items():
        print(name, node)
