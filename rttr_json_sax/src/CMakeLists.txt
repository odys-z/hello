# Define the core logic as a library
add_library(anson INTERFACE)

# Add include directories so tests can find your headers
# target_include_directories(json_sax_lib INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(anson INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

# Link the required external libraries
target_link_libraries(anson INTERFACE 
    RTTR::Core
    nlohmann_json::nlohmann_json
)

# If your library needs RTTR, link it here
# target_link_libraries(anson INTERFACE RTTR::Core)
