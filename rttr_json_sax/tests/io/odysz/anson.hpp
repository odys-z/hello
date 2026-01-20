#pragma once
#include <string>
#include <iostream>
// #include <rttr/type.h>
#include <rttr/registration>
#include <nlohmann/json.hpp>

#define NL '\n'

using namespace  std ;

namespace anson {
class Anson {
public:
    std::string type;

    Anson() { cout << "defalut contructor" << NL ; }
    Anson(string t) : type(t) { cout << "override contructor, type = " << t << NL ; }

    RTTR_ENABLE()
};
}

// RTTR_REGISTRATION {
//     using namespace rttr;
//     using namespace anson;
//     rttr::registration::class_<Anson>("anson::Anson")
//         .constructor<std::string>()
//          (policy::ctor::as_std_shared_ptr,
//           default_arguments(string("--")) )
//         .property("type", &Anson::type)
//         ;
// }

