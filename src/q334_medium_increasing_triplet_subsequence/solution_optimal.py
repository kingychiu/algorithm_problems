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
            For example with 20, 100, 10, 12, 5, 13. 
            The final values are 5, 12, 13,
            while the correct triplet should be 10, 12, 13.
            
            Generally speaking, it is not an issue.
            - If the "first" got replaced, the current "second" are still larger than all historical "first" values:
            current second (12) > current first (5) > all historical first values (... 10)

            - If the "first" and "second" smallest got replaced: then we are looking at a entirely new triplet

            - When we reach the else case, we will have:
            current_third (13) > current second (12) > current first (5) > all historical first values. (... 10),
            the true "first" element of the triplets is hidden in the historical first values.
            """
            if num <= first_smallest:
                first_smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        return False


# @lc code=end
