#pragma once

#include <string>
#include <iostream>
#include <nlohmann/json.hpp>
#include <entt/meta/meta.hpp>
#include <entt/entt.hpp>

using namespace  std ;

namespace anson {


class JsonOpt;// : public Anson { };

class IJsonable {

public:
    virtual IJsonable* toBlock(ostream& os, JsonOpt& opts);

    /** @see #toBlock(OutputStream, JsonOpt...) */
    virtual string toBlock(JsonOpt& opt) {
        // ByteArrayOutputStream bos = new ByteArrayOutputStream();
        // toBlock(bos, opt);
        // return bos.toString(StandardCharsets.UTF_8.name());
        std::ostringstream bos;
        toBlock(bos, opt);
        return bos.str();
    }

    /**
     * @param buf
     * @return this
     * @throws IOException
     * @throws AnsonException
     */
    virtual IJsonable* toJson(string& buf);

    int tree_sitter_test() { return 0; }
    char& s_test0;
    char& s_test1;
    char** s_test2;
    char** s_test3;
};

template<typename T>
class EnTTSaxParser;

/**
 * @brief The Anson class
 * java type: io.odysz.anson.Anson
 */
class Anson {
public:
    inline static const string _type_ = "io.odysz.anson.Anson";
    std::string type;

    Anson() { cout << "defalut contructor" << endl ; }
    Anson(string t) : type(t) { cout << "override constructor, type = " << t << endl ; }
    
    template <typename T>
    static bool from_json(const string& json, T& an) {
        EnTTSaxParser<T> handler{an};
        return nlohmann::json::sax_parse(json, &handler);
    }
};

class SemanticObject : public Anson {
public:
    map<string, any> data;
};
}

