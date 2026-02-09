#pragma once
#include <entt/meta/factory.hpp>
#include <entt/meta/meta.hpp>

#include "anson.h"
#include "jprotocol.h"

namespace anson {
inline void register_meta() {
    using namespace entt::literals;

    entt::meta_factory<anson::Port>()
        .type("Port"_hs)
        .data<anson::Port::query>("query"_hs, "query")
        .data<anson::Port::update>("update"_hs, "update")
        .data<anson::Port::ok>("ok"_hs, "ok")
        .data<anson::Port::echo>("echo"_hs, "echo")
        .data<anson::Port::docstier>("docstier"_hs, "docstier")
        .data<anson::Port::exSession>("exSession"_hs, "exSession")
        .data<anson::Port::exSemantic>("exSemantic"_hs, "exSemantic")
        .data<anson::Port::exIo>("exIo"_hs, "exIo")
        .data<anson::Port::exTransct>("exTransct"_hs, "exTransct")
        .data<anson::Port::exDA>("exDA"_hs, "exDA")
        .data<anson::Port::ext>("ext"_hs, "ext")
        .data<anson::Port::exGeneral>("exGeneral"_hs, "exGeneral")
        ;
    entt::meta_factory<anson::MsgCode>()
        .type("MsgCode"_hs)
        .data<anson::MsgCode::query>("query"_hs, "query")
        .data<anson::MsgCode::update>("update"_hs, "update")
        .data<anson::MsgCode::ok>("ok"_hs, "ok")
        .data<anson::MsgCode::echo>("echo"_hs, "echo")
        .data<anson::MsgCode::docstier>("docstier"_hs, "docstier")
        .data<anson::MsgCode::exSession>("exSession"_hs, "exSession")
        .data<anson::MsgCode::exSemantic>("exSemantic"_hs, "exSemantic")
        .data<anson::MsgCode::exIo>("exIo"_hs, "exIo")
        .data<anson::MsgCode::exTransct>("exTransct"_hs, "exTransct")
        .data<anson::MsgCode::exDA>("exDA"_hs, "exDA")
        .data<anson::MsgCode::ext>("ext"_hs, "ext")
        .data<anson::MsgCode::exGeneral>("exGeneral"_hs, "exGeneral")
        ;
    entt::meta_factory<anson::IJsonable>().type("IJsonable"_hs);
    entt::meta_factory<anson::Anson>().type("Anson"_hs);
    entt::meta_factory<anson::SemanticObject>().type("SemanticObject"_hs);
    entt::meta_factory<anson::AnsonBody>().type("AnsonBody"_hs);
    entt::meta_factory<anson::EchoReq>().type("EchoReq"_hs);
    entt::meta_factory<anson::AnsonResp>().type("AnsonResp"_hs);
    entt::meta_factory<anson::AnsonMsg>().type("AnsonMsg"_hs);
    entt::meta_factory<anson::UserReq>().type("UserReq"_hs);
    entt::meta_factory<anson::OnError>().type("OnError"_hs);
}
}