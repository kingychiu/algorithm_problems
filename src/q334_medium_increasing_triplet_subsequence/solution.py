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
        if len(nums) < 3:
            return False

        post_maxes = [float("-inf")] * len(nums)  # including itself
        for idx in range(len(nums) - 1, -1, -1):
            post_maxes[idx] = (
                max(nums[idx], post_maxes[idx + 1])
                if idx < (len(nums) - 1)
                else nums[idx]
            )

        i, j, k = 0, 1, 2
        while i < j < k and k < len(nums):
            updated = False
            # Match
            if nums[i] < nums[j] < nums[k]:
                return True

            # push for nums[i] < nums[j]
            if nums[i] >= nums[j]:
                i += 1
                updated = True
                # push more for i < j < k
                if i == j and j < len(nums) - 1:
                    j += 1
                if j == k and k < len(nums) - 1:
                    k += 1
            # check do we move j or k
            elif nums[j] >= post_maxes[j]:
                j += 1
                updated = True
                if j == k and k < len(nums) - 1:
                    k += 1
            elif k < len(nums) - 1:
                updated = True
                k += 1

            if not (i < j < k) or not updated:
                break

        return False


# @lc code=end
