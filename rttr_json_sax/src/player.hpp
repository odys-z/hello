#pragma once
#include <rttr/registration>
#include <string>

struct Player {
    std::string name;
    int level;
    RTTR_ENABLE()
};
