field_decl_list: str = """
        (enum_specifier 
            name: (type_identifier) @enum_name
            body: (enumerator_list (enumerator name: (identifier) @enum_val)))

        (class_specifier
            name: (type_identifier) @class_name
            body: (field_declaration_list (field_declaration) @field))
"""
field_id_isfunc: str = """
    (enum_specifier 
        name: (type_identifier) @enum_name
        body: (enumerator_list (enumerator name: (identifier) @enum_val)))

    (class_specifier
        name: (type_identifier) @class_name
        (base_class_clause (type_identifier) @base_name)?
        body: (field_declaration_list 
            [
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

                ;; 2. Capture Function Prototypes (without bodies)
                (field_declaration
                    type: (_) @func_ret_type
                    declarator: (function_declarator
                        declarator: [
                            (field_identifier) @ctor_name
                            (identifier) @ctor_name
                        ]
                        parameters: (parameter_list) @ctor_params)) @is_func

                ;; 3. Capture Function Definitions (with bodies)
                (function_definition
                    type: (_)? @func_ret_type
                    declarator: (function_declarator
                        declarator: [
                            (field_identifier) @ctor_name
                            (identifier) @ctor_name
                        ]
                        parameters: (parameter_list) @ctor_params)) @is_func
            ]
        ))
"""

fieldeclpointer_funcdecl_fdretdecl : str = """
    (enum_specifier 
        name: (type_identifier) @enum_name
        body: (enumerator_list (enumerator name: (identifier) @enum_val)))

    (class_specifier
        name: (type_identifier) @class_name
        (base_class_clause (type_identifier) @base_name)?
        body: (field_declaration_list 
            [
                ;; 1. Variable fields (must not be a function_declarator)
                (field_declaration 
                    (storage_class_specifier)* @storage
                    type: (type_identifier) @field_type
                    declarator: [
                        (identifier) 
                        (pointer_declarator) 
                        (reference_declarator)
                    ] @field_decl)

                ;; 2. Function declarations (prototypes)
                (field_declaration
                    type: (_) @func_ret_type
                    declarator: (function_declarator
                        declarator: (identifier) @ctor_name
                        parameters: (parameter_list) @ctor_params))

                ;; 3. Function definitions (with bodies)
                (function_definition
                    type: (_)? @func_ret_type
                    declarator: (function_declarator
                        declarator: (identifier) @ctor_name
                        parameters: (parameter_list) @ctor_params))
            ]
        ))
"""

fieldecl_funcdecl_funcdef : str = """
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
                    type: (_) @field_type
                    ;; Capture the whole declarator tree
                    declarator: (_) @field_decl)
                
                ;; Capture constructors
                (declaration
                    declarator: (function_declarator
                        declarator: (identifier) @ctor_name
                        parameters: (parameter_list) @ctor_params))
                        
                ;;
                (function_definition
                    declarator: (function_declarator
                        declarator: (identifier) @ctor_name
                        parameters: (parameter_list) @ctor_params))
            ]
        ))
"""