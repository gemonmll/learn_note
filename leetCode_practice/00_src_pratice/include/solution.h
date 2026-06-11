#ifndef SOLUTION_H
#define SOLUTION_H

#include <vector>
#include <string>

// --- LeetCode 解题类的声明 ---
class Solution
{
public:
    // 在这里声明你在 LeetCode 上需要实现的函数
    // 例如: 题 1. 两数之和
    std::vector<int> twoSum(std::vector<int> &nums, int target);

    // 当你解决新问题时，可以在这里添加新的函数声明
    // 例如: 题 2. 两数相加
    // struct ListNode; // 如果需要，可以提前声明依赖的结构体
    // ListNode* addTwoNumbers(ListNode* l1, ListNode* l2);
};

#endif // SOLUTION_H