#include <gtest/gtest.h>
#include "../src/math_utils.h"   // adjust path if needed

// Basic test suite
TEST(MathUtilsTest, HandlesEvenNumbers) {
    EXPECT_TRUE(is_even(0));     // 0 is even
    EXPECT_TRUE(is_even(2));
    EXPECT_TRUE(is_even(-4));
    EXPECT_TRUE(is_even(42));
}

TEST(MathUtilsTest, HandlesOddNumbers) {
    EXPECT_FALSE(is_even(1));
    EXPECT_FALSE(is_even(7));
    EXPECT_FALSE(is_even(-3));
}

// Optional: one more style using ASSERT (stops on first failure)
TEST(MathUtilsTest, EdgeCases) {
    ASSERT_TRUE(is_even(0)) << "Zero should be even!";  // ASSERT stops test if fails
    EXPECT_EQ(true, is_even(1000000));
    EXPECT_NE(true, is_even(999999));   // not equal to true → i.e. false
}