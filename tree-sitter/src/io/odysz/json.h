/**
 * The eqivalent of gen.antlr.json + JSONAnsonListener
 */
#pragma once

#include <entt/meta/meta.hpp>
#include <entt/entt.hpp>

#include "anson.h"
#include "jprotocol.h"

namespace anson {

inline void register_meta() {
    using namespace entt::literals;

    entt::meta_factory<anson::Anson>()
        .type("Anson"_hs)
        .ctor<>()
        .ctor<const std::string&>()
        .data<&anson::Anson::type>("type"_hs, "type")
        ;

    entt::meta_factory<anson::SemanticObject>()
        .type("SemanticObject"_hs)
        .ctor<>()
        .base<anson::Anson>()
        ;

    entt::meta_factory<anson::AnsonBody>()
        .type("AnsonBody"_hs)
        .ctor<const std::string&>()
        .ctor<const std::string&, const std::string&>()
        .base<anson::Anson>()
        .data<&anson::AnsonBody::a>("a"_hs, "a")
        ;

    entt::meta_factory<anson::EchoReq>()
        .type("EchoReq"_hs)
        .ctor<>()
        .ctor<const std::string&>()
        .base<anson::AnsonBody>()
        .data<&anson::EchoReq::echo>("echo"_hs, "echo")
        ;

    entt::meta_factory<anson::UserReq>()
        .type("UserReq"_hs)
        .ctor<const std::string&>()
        .base<anson::AnsonBody>()
        .data<&anson::UserReq::data>("data"_hs, "data")
        ;

    entt::meta_factory<anson::Port>()
        .type("Port"_hs)
        .data<anson::Port::query>("query"_hs, "query")
        .data<anson::Port::update>("update"_hs, "update")
        .data<anson::Port::echo>("echo"_hs, "echo")
        ;

    // Register MsgCode enum
    entt::meta_factory<anson::MsgCode>()
        .type("MsgCode"_hs)
        .data<anson::MsgCode::ok>("ok"_hs, "ok")
        .data<anson::MsgCode::exSession>("exSession"_hs, "exSession")
        .data<anson::MsgCode::exSemantic>("exSemantic"_hs, "exSemantic")
        .data<anson::MsgCode::exIo>("exIo"_hs, "exIo")
        .data<anson::MsgCode::exTransct>("exTransct"_hs, "exTransact")
        .data<anson::MsgCode::exDA>("exDA"_hs, "exDA")
        .data<anson::MsgCode::exGeneral>("exGeneral"_hs, "exGeneral")
        .data<anson::MsgCode::ext>("ext"_hs, "ext")
        ;

    entt::meta_factory<anson::AnsonResp>()
        .type("AnsonResp"_hs)
        .ctor<>()
        .ctor<const std::string&>()
        .base<anson::AnsonBody>()
        .data<&anson::AnsonResp::code>("code"_hs, "code")
        ;

    // Register AnsonMsg template (example for EchoReq)
    entt::meta_factory<anson::AnsonMsg<anson::EchoReq>>()
        .type("AnsonMsgEcho"_hs)
        .ctor<anson::Port>()
        .base<anson::Anson>()
        .data<&anson::AnsonMsg<anson::EchoReq>::port>("port"_hs, "port")
        .data<&anson::AnsonMsg<anson::EchoReq>::body>("body"_hs, "body");


}

}
