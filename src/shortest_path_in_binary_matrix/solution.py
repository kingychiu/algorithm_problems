"""
    https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""


from collections import deque


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def get_submission(self, grid: list[list[int]]) -> int:
        # pylint: disable=no-self-use
        """
        Return the length of the shortest such clear path from top-left to bottom-right.
        If such a path does not exist, return -1.
        """
        # BFS setup
        queue: deque[tuple[int, ...]] = deque([(0, 0)])
        visited: set[tuple[int, ...]] = set()
        target_row = len(grid) - 1

        # Empty grid
        if target_row == -1:
            return 0
        # Invalid starting point
        if grid[0][0] == 1:
            return -1
        target_col = len(grid[0]) - 1

        # Possible directions
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]
        cost = 0
        while queue:
            cost += 1
            next_queue: deque[tuple[int, ...]] = deque()
            while queue:
                row, col = queue.popleft()
                if row == target_row and col == target_col:
                    return cost

                for drow, dcol in directions:
                    nrow = row + drow
                    ncol = col + dcol
                    if (
                        target_col >= ncol >= 0
                        and target_row >= nrow >= 0
                        and grid[nrow][ncol] == 0
                        and (nrow, ncol) not in visited
                    ):
                        visited.add((nrow, ncol))
                        next_queue.append((nrow, ncol))
            queue = next_queue
        return -1
