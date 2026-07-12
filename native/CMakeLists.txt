cmake_minimum_required(VERSION 3.20)

project(methys_core VERSION 0.1.0 LANGUAGES C)

add_library(methys_core SHARED
    src/methys_core.c
    src/methys_database.c
)
add_library(methys::core ALIAS methys_core)

target_include_directories(methys_core
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)

target_compile_features(methys_core PRIVATE c_std_11)

set_target_properties(methys_core PROPERTIES
    C_VISIBILITY_PRESET hidden
    VERSION ${PROJECT_VERSION}
    SOVERSION 0
)
