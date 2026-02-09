# About

The Tree-sitter is a C++ language parser that based on AST and C++ syntax definition.
This folder is a learning snapshot showing how to use Tree-sitter's query language.

The running results should be:

```
    $ src\.venv\Scripts\python.exe src\gen-registry-8.py 
    IJsonable Func toBlock
    IJsonable Func tree_sitter_test
    IJsonable Memb char & s_test0
    IJsonable Memb char & s_test1
    IJsonable Memb char ** s_test2
    IJsonable Memb char ** s_test3
    Anson S _type_
    Anson Memb std::string type
    Anson Ctor Anson []
    Anson Ctor Anson ['string']
    SemanticObject Memb map<string, any> data
    AnsonBody S _type_
    AnsonBody Memb string a
    AnsonBody Ctor AnsonBody []
    AnsonBody Ctor AnsonBody ['string']
    AnsonBody Ctor AnsonBody ['string', 'string']
    EchoReq S _type_
    EchoReq Memb string echo
    EchoReq Ctor EchoReq []
    EchoReq Ctor EchoReq ['string']
    UserReq Memb map<string, any> data
    UserReq Ctor UserReq ['string']
    AnsonResp Memb MsgCode code
    AnsonResp Ctor AnsonResp []
    AnsonResp Ctor AnsonResp ['string']
    OnError Func err

    Process finished with exit code 0
```

* [LLM Programming Process Record](https://gemini.google.com/share/064a91f9f269)

* [Tree-sitter Query Syntax Definition at Github](https://github.com/tree-sitter/tree-sitter-cpp/blob/master/src/node-types.json")

