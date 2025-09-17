# CMake 最低版本要求
cmake_minimum_required(VERSION 3.10)

# 项目名称
project(LeetCodeSolutions CXX)

# 设置 C++ 标准为 C++17，这是目前 LeetCode 支持的主流版本之一
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 在发布模式下启用优化，在调试模式下启用调试信息
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
set(CMAKE_CXX_FLAGS_DEBUG "-g -Wall -Wextra -pedantic")

# 设置默认构建类型为 Debug，方便调试
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

# 包含头文件目录
include_directories(include)

# ------------------------------------------------------------------
#  核心部分：指定你要编译和测试的题目文件
#  你只需要修改这里的 "0001_two_sum.cpp" 为你想要测试的题目文件名即可
# ------------------------------------------------------------------
set(CURRENT_SOLUTION_SOURCE "solutions/0001_two_sum.cpp")

# 添加主程序和当前的解题源文件到项目中
add_executable(leetcode_runner main.cpp ${CURRENT_SOLUTION_SOURCE})

# (可选) 如果你的项目依赖了其他库（例如 GTest），可以在这里添加
# find_package(GTest REQUIRED)
# target_link_libraries(leetcode_runner GTest::GTest GTest::Main)

# 输出提示信息，方便确认当前编译的是哪个文件
message(STATUS "Building executable 'leetcode_runner' with solution: ${CURRENT_SOLUTION_SOURCE}")