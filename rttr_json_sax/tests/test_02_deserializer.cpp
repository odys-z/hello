#include <gtest/gtest.h>
#include "io/odysz/rttr.hpp"

using namespace std;
using namespace rttr;
using namespace anson;

TEST(Anson, Base) {

    type t = type::get_by_name("anson::Anson");
    rttr::variant v = t.create({std::string("io.odysz.anson.Anson")});
    shared_ptr<anson::Anson> ans = v.convert<shared_ptr<anson::Anson>>();
    cout << "[1] ans.type: " << ans->type << NL;
    ASSERT_EQ("io.odysz.anson.Anson", ans->type);

    std::string json_input = R"({"type": "input"})";
    // 1. dereferencing the shared_ptr, which results in a reference to the anson::Anson object
    // 2. Passing *ans to rttr::instance creates an instance that refers to the original object (shallow copy)
    RttrSaxHandler handler(*ans);

    cout << "[2] " << json_input << NL;
    bool result = nlohmann::json::sax_parse(json_input, &handler);
    
    ASSERT_TRUE(result);
    ASSERT_EQ("input", ans->type);
}

TEST(Anson, AnsonBody) {

    type b = type::get_by_name("anson::AnsonBody");
    rttr::variant v = b.create({std::string("r/ds")});
    shared_ptr<anson::AnsonBody> anb = v.convert<shared_ptr<anson::AnsonBody>>();
    cout << "[1] anb.type: " << anb->type << NL;
    ASSERT_EQ("io.odysz.jprotocol.AnsonBody", anb->type);
    ASSERT_EQ("r/ds", anb->a);

    std::string json_input = R"({"type": "input", "a": "r/query"})";
    RttrSaxHandler handler(*anb);

    cout << "[2] " << json_input << NL;
    bool result = nlohmann::json::sax_parse(json_input, &handler);
    cout << "[3] ok: " << result << ", type: " << anb->type << ", a: " << anb->a << NL;
    ASSERT_TRUE(result);
    ASSERT_EQ("input", anb->type);
    ASSERT_EQ("r/query", anb->a);
}

TEST(Anson, AnsonMsg) {

    using Req = AnsonMsg<EchoReq>;

    // type m = type::get_by_name("anson::AnsonMsg");
    type m = type::get<anson::AnsonMsg<EchoReq>>();
    rttr::variant v = m.create({std::string("echo")});
    shared_ptr<Req> msg = v.convert<shared_ptr<Req>>();
    cout << "[1] msg.port: " << msg->port << NL;
    ASSERT_EQ("io.odysz.jprotocol.AnsonMsg", msg->type);
    ASSERT_EQ("echo", msg->port);

}
