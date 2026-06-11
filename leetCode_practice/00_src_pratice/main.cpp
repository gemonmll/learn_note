#include <iostream>
#include "solution.h" // [修改] 包含 solution.h 头文件

int main()
{
    // 创建 Solution 类的实例
    Solution sol;

    // ==========================================================
    // 在这里编写你的测试代码
    // ==========================================================

    // 示例：测试 "两数之和" (solutions/0001_two_sum.cpp)
    std::cout << "--- Running Test for Problem 1: Two Sum ---" << std::endl;

    // 测试用例 1
    std::vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    std::cout << "Test Case 1: nums = [2, 7, 11, 15], target = 9" << std::endl;
    std::vector<int> result1 = sol.twoSum(nums1, target1);

    if (result1.size() == 2)
    {
        std::cout << "Result: [" << result1[0] << ", " << result1[1] << "]" << std::endl;
        std::cout << "Expected: [0, 1] or [1, 0]" << std::endl;
    }
    else
    {
        std::cout << "No solution found." << std::endl;
    }
    std::cout << "---------------------------------------------" << std::endl;

    // 测试用例 2
    std::vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    std::cout << "Test Case 2: nums = [3, 2, 4], target = 6" << std::endl;
    std::vector<int> result2 = sol.twoSum(nums2, target2);

    if (result2.size() == 2)
    {
        std::cout << "Result: [" << result2[0] << ", " << result2[1] << "]" << std::endl;
        std::cout << "Expected: [1, 2] or [2, 1]" << std::endl;
    }
    else
    {
        std::cout << "No solution found." << std::endl;
    }
    std::cout << "---------------------------------------------" << std::endl;

    // ==========================================================
    // 测试代码结束
    // ==========================================================

    return 0;
}