#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#


# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        [2, 3, 5, 1, 3], 3, max: 5

        [5, 3, 5, 1, 3] -> T
        [2, 6, 5, 1, 3] -> T
        [2, 3, 8, 1, 3] -> T
        [2, 3, 5, 4, 3] -> F
        [2, 3, 5, 1, 6] -> T
        """
        result = [False] * len(candies)
        max_num_candies = max(candies)  # O(N)
        for i, num_candies in enumerate(candies):  # O(N)
            if num_candies + extraCandies >= max_num_candies:
                result[i] = True
        return result


# @lc code=end
