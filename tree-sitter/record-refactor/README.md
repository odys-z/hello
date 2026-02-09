# LLM Refactoring

LLM Programming Record: https://gemini.google.com/share/7281e5a2fe5c

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
