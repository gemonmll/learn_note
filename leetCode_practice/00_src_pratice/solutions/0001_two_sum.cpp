#include <vector>
#include <unordered_map>
#include "solution.h" // 包含类的声明

// 这是 LeetCode 题解类的具体实现
// 注意函数签名需要和 solution.h 中声明的完全一致

/**
 * @brief 给定一个整数数组 nums 和一个整数目标值 target，
 * 请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
 * @param nums 整数数组
 * @param target 目标值
 * @return 包含两个下标的向量
 */
std::vector<int> Solution::twoSum(std::vector<int> &nums, int target)
{
    // 使用哈希表来存储数字及其索引
    std::unordered_map<int, int> num_map;

    for (int i = 0; i < nums.size(); ++i)
    {
        int complement = target - nums[i];

        // 检查差值是否在哈希表中
        if (num_map.count(complement))
        {
            // 如果存在，则返回差值的索引和当前数字的索引
            return {num_map[complement], i};
        }

        // 如果不存在，将当前数字和它的索引存入哈希表
        num_map[nums[i]] = i;
    }

    // 如果没有找到解，返回一个空向量
    return {};
}

// 如果你在 solution.h 中声明了其他函数，
// 也需要在这里实现它们，例如：
// ListNode* Solution::addTwoNumbers(ListNode* l1, ListNode* l2) {
//     // ... 实现细节 ...
// }