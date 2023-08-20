#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        results = []
        prefix_prod = 1
        for i in range(len(nums)):
            results.append(prefix_prod)
            prefix_prod *= nums[i]

        postfix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= postfix_prod
            postfix_prod *= nums[i]
        return results


# @lc code=end
