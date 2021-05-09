"""
    https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List, Tuple, Optional

import math

class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    def trap(self, height: List[int]) -> int:
        # pylint: disable=no-self-use
        """
            Given n non-negative integers representing an elevation map where the width of each bar is 1,
            compute how much water it can trap after raining.
        """

        start = 0
        temp_count = 0
        trapped_count = 0
        for end in range(len(height)):
            if height[end] < height[start]:
                # temp water trapped
                temp_count += height[start] - height[end]
            else:
                # actually trapped
                trapped_count += temp_count
                start = end
                temp_count = 0

        # final clean up
        if temp_count != 0:
            temp_count = 0
            prev_start = start
            start = end
            for end in range(len(height) - 1, prev_start - 1, -1):
                if height[end] < height[start]:
                    # temp water trapped
                    temp_count += height[start] - height[end]
                else:
                    # actually trapped
                    trapped_count += temp_count
                    start = end
                    temp_count = 0
        return trapped_count
