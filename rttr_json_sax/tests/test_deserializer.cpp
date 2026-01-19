#include <gtest/gtest.h>
#include "player.hpp"
#include "rttr_sax_handler.hpp"

// Re-register or ensure registration for the test environment
RTTR_REGISTRATION {
    rttr::registration::class_<Player>("Player")
        .property("name", &Player::name)
        .property("level", &Player::level);
}

TEST(DeserializerTest, BasicPlayerMapping) {
    Player p;
    std::string json_input = R"({"name": "TestBot", "level": 10})";
    RttrSaxHandler handler(p);
    
    bool result = nlohmann::json::sax_parse(json_input, &handler);
    
    ASSERT_TRUE(result);
    EXPECT_EQ(p.name, "TestBot");
    EXPECT_EQ(p.level, 10);
}

TEST(DeserializerTest, MissingPropertyDoesNotCrash) {
    Player p;
    p.name = "Original";
    std::string json_input = R"({"unknown_field": "ignore_me"})";
    RttrSaxHandler handler(p);
    
    bool result = nlohmann::json::sax_parse(json_input, &handler);
    
    ASSERT_TRUE(result);
    EXPECT_EQ(p.name, "Original"); // Should remain unchanged
}
