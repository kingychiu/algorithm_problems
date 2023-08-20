#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Check if there exist 3 indices i < j < k, such that nums[i] < nums[j] nums[k].
        """
        first_smallest = float("+inf")
        second_smallest = float("+inf")
        for num in nums:
            """
            if the triplet values are truely monotonic increasing,
            num will match the the cases below 1 by 1.
            EX: 1, 2, 3
            1: matches 1st
            2: matches 2nd
            3: matches 3rd
            EX: 4, 1, 3, 2, 4
            4: matches 1st
            1: matches 1st (replace 4)
            3: matches 2nd
            2: matches 2nd (replace 3)
            4" matches 3rd
            """
            if num <= first_smallest:
                first_smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        return False


# @lc code=end
