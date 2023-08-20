#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        num_beds = len(flowerbed)
        for i in range(num_beds):
            spot_empty = flowerbed[i] == 0
            left_empty = i == 0 or flowerbed[i - 1] == 0
            right_empty = i == (num_beds - 1) or flowerbed[i + 1] == 0
            if spot_empty and left_empty and right_empty:
                n -= 1
                flowerbed[i] = 1
            if n <= 0:
                return True

        return False


# @lc code=end
