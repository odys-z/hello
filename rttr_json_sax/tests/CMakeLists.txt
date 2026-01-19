include(GoogleTest)

# Create the test executable
add_executable(
    anson_tests
    test_deserializer.cpp
)

# Link to our source library and GoogleTest
# gtest_main provides the main() function for the tests
target_link_libraries(anson_tests PRIVATE 
    json_sax_lib 
    gtest_main
)

# Discover and add tests to CTest
gtest_discover_tests(anson_tests)
