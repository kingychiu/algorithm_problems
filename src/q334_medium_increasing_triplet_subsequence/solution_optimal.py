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
            if the triplet values are truly monotonic increasing,
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
            
            At the end the first, second, third values here MIGHT NOT BE the triplet we are looking for.
            For example with 20,100,10,12,5,13. the final values are 5,12,13.
            But because of the 2nd value is 12, we can ensure every first second smallest values are also smaller than 12.
            
            Generally speaking,
            - Every historical first_smallest must smaller than the latest second_smallest
            - Every historical second_smallest must smaller than the latest third (returned already).
            """
            if num <= first_smallest:
                first_smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        return False


# @lc code=end
