# About

[LLM Programming Record](https://gemini.google.com/share/7281e5a2fe5c)

# LLM can create illusions

* Example:

  While using *CppHeaderParser* for generating parse, asked:

  ```
    config file gen.json:

        { "type": "io.oz.gen.cmake.settings",
           "src": ["io/odysz/anson.h","io/odysz/jprotocol.h"],
            "gen": "json.h"
        }

    use this lib to load the file, gen.json: https://github.com/odys-z/antson/tree/master/py3 (stop if you don't understand)

    modify this if you understand my question: https://github.com/odys-z/antson/tree/master/semantics.py3 
  ```

  The output even confused the Anson repository's creator:

  ```
    1 I don't think there are anson.util and AnsonProtocol. You need carefully have a look at the tests. https://github.com/odys-z/antson/tree/master/py3/test

    2. The deserialized type must be adde to semantics.py3, https://github.com/odys-z/antson/tree/master/semantics.py3 (I own the repo, you tell me how to upgrade)

    try again.
  ```

  LLM can be take as failed at this question. For human, he should first questioning the deserialization
  process or the dependency of Semantics.py3. (The Agent works as an itorating process of thinking or optimization?)

# LLM Abstracting Abilities

* Ask:

  ```
    Now let's base our talk on this file. Handling the template classes, say, AnsonMsg. Later when found somewhere it is used, say AnosnMsg<EchoReq>, generate entt registration like this:

        entt::meta_factory<anson::EchoReq>()
            .type("EchoReq"_hs)
            .ctor<>()
            .ctor<const std::string&>()
            .base<anson::AnsonBody>()
            .data<&anson::EchoReq::echo>("echo"_hs, "echo");
  ```

  LLM results can be this:

  ```
    # Parser
    if base == "AnsonBody" and cname not in anson_body_subclasses:
        anson_body_subclasses.append((cname, base))

    # Generator
    # Specialized AnsonMsg Template Registration
    for sub, base in anson_body_subclasses:
        output.append(f"{indent}// Specialized AnsonMsg for {sub}")
        output.append(f"{indent}entt::meta_factory<{namespace}::AnsonMsg<{namespace}::{sub}>>()")
        output.append(f"{indent * 2}.type(\"AnsonMsg{sub}\"_hs)")
        output.append(f"{indent * 2}.base<{namespace}::{base}>()")

        # TODO FIXME LLM Error
        output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::port>(\"port\"_hs, \"port\")")
        output.append(f"{indent * 2}.data<&{namespace}::AnsonMsg<{namespace}::{sub}>::body>(\"body\"_hs, \"body\");\n")
  ```

  It shouldn't be handled case by case. My hypothesis is that LLM cannot apply OOP principals to
  the attentions collected by it's learnt model.


# LLM Refactoring

* Ask Gemini:

    Let's refoctor function parse_anson(). See the comments.
    You should break the large block into functions, use the designed data
    structure at the beginning section, e.g. MetaEnum and MetaClass. Try it.

* Some Errors:

1. Using the wrong query string variable.

   The uploaded source code uses `field_id_isfunc` as the query string. The LLM answer uses `fieldecl_funcdecl_funcdef`,
   which is not presented in the AI talk previously, but should be close to some early used query string.

   Is this showing that LLM cannot understand the logic flow but still able to get close to the runnable result?

2. Wrong query definition itself.

   2.1 Impossible *reference_declarator* by tree-sitter. (An early error in the same talk)

       (reference_declarator declarator: (field_identifier) @field_name)    # Tree-sitter says impossible.
       (pointer_declarator declarator: (field_identifier) @field_name)

       -> 
       (reference_declarator (field_identifier) @field_name)                 # Check ../node-types.json
       (pointer_declarator declarator: (field_identifier) @field_name)

    2.2 Missleading query structure.
     
        ;; 1. Capture Data Members specifically
        (field_declaration 
            (storage_class_specifier)* @storage
            type: (_) @field_type
            declarator: [
                (field_identifier) @field_name
                (reference_declarator (field_identifier) @field_name)
                (pointer_declarator declarator: (field_identifier) @field_name)
                (pointer_declarator declarator: (pointer_declarator declarator: (field_identifier) @field_name))
                ;; (pointer_declarator declarator: (pointer_declarator declarator: (pointer_declarator declarator: field_identifier) @field_name)))
            ] @field_decl) @is_field
        
      This always return captures without 'field_name'.

      correction:

        ;; 1. Capture Data Members specifically
        (field_declaration 
            (storage_class_specifier)* @storage
            type: (type_specifier) @field_type
            declarator: [
                ((field_identifier) @field_name) @field_register
                (reference_declarator (field_identifier) @field_name) @field_register
                (pointer_declarator declarator: (field_identifier) @field_name) @field_register
                (pointer_declarator declarator: (pointer_declarator declarator: (field_identifier) @field_name)) @field_register
                ;; (pointer_declarator declarator: (pointer_declarator declarator: (pointer_declarator declarator: field_identifier) @field_name)))
            ] @field_decl) @is_field
    
      Console Print:

        Field? s_test0 char & s_test0
        Field? s_test1 char & s_test1
        Field? s_test2 char ** s_test2
        Field? s_test3 char ** s_test3
        Field? _type_ string _type_
        Ignore static string b'_type_'
        Field? type std::string type
        Field? data map<string, any> data
        Field? _type_ string _type_
        Ignore static string b'_type_'
        Field? a string a
        Field? _type_ std::string _type_
        Ignore static std::string b'_type_'
        Field? echo string echo
        Field? data map<string, any> data
        Field? code MsgCode code
        Port MetaEnum(verbose=False, __type__='__main__.MetaEnum', etype='Port', enums=['query', 'update', 'echo', 'docstier'])
        MsgCode MetaEnum(verbose=False, __type__='__main__.MetaEnum', etype='MsgCode', enums=['ok', 'exSession', 'exSemantic', 'exIo', 'exTransct', 'exDA', 'exGeneral', 'ext'])

      Can this be used to show that LLM is acctually knowing nothing of the query syntax but can get close to the correct answer?

3. Other issues

   3.1 The functions API (signature) can be optimized
   
      ```
      if cname not in found_classes:
          base = caps['base_name'][0].text.decode('utf8') if 'base_name' in caps else None
          found_classes[cname] = MetaClass(cname=cname, base=base)

      extract_class_member(caps, cname, found_classes[cname])
      ```
    
    Should this can be better?
      
      ```
      # create MetaClass if not exists, put into found_classes
      extract_class_member(found_classes, caps)
      ```
