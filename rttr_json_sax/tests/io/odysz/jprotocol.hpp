#pragma once

#include "anson.hpp"

namespace anson {

class AnsonBody : public anson::Anson {
public:
    string a;

    AnsonBody(string a) : Anson("io.odysz.jprotocol.AnsonBody") , a(a) {}

    AnsonBody(string a, string type) : Anson(type), a(a) {}
    RTTR_ENABLE(Anson)
};

// template<typename T>
class AnsonMsg: public Anson {
public:
    // vector<T&> body;

    string port;

    AnsonMsg(string port) : Anson("io.odysz.jprotocol.AnsonMsg"), port(port) {}

    RTTR_ENABLE()
};

class EchoReq: public AnsonBody {
public:
    string echo;

    EchoReq(string echo) : AnsonBody("r/query", "io.odysz.jprotocol.EchoReq"), echo(echo) {}

    RTTR_ENABLE()
};
}

