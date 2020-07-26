"""
    https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
from collections import defaultdict
from typing import List, DefaultDict, Tuple


class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    def get_submission(self, grid: List[List[int]]) -> int:
        # pylint: disable=no-self-use
        """
            Return the length of the shortest such clear path from top-left to bottom-right.
            If such a path does not exist, return -1.
        """
        # BFS setup
        queue: List[Tuple[int, int, int]] = [(0, 0, 1)]
        visited: DefaultDict[Tuple[int, int], bool] = defaultdict(lambda: False)
        target_y = len(grid) - 1
        if target_y == -1:
            return 0
        if grid[0][0] == 1:
            return -1
        target_x = len(grid[0]) - 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while queue:
            # BFS dequeue
            x, y, cost = queue.pop(0)  # pylint: disable=invalid-name
            if x == target_x and y == target_y:
                return cost
            for dir_x, dir_y in directions:
                new_x = x + dir_x
                new_y = y + dir_y
                if target_x >= new_x >= 0 and target_y >= new_y >= 0 \
                        and grid[new_y][new_x] == 0 and not visited[(new_x, new_y)]:
                    visited[(new_x, new_y)] = True
                    queue.append((new_x, new_y, cost + 1))
        return -1
