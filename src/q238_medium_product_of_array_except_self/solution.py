#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        results = []
        accum = 1
        for i in range(len(nums)):
            results.append(accum)
            accum *= nums[i]

        accum = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= accum
            accum *= nums[i]
        return results


# @lc code=end
