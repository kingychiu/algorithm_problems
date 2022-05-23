"""
    https://leetcode.com/problems/rotting-oranges/
"""

from collections import deque


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def next_moves(self, row, col, grid_width, grid_height) -> list[tuple[int, int]]:
        # pylint: disable=no-self-use
        """Get next moves of the flooding"""
        next_nodes = []
        can_go_up = row > 0
        can_go_down = row < grid_height - 1
        can_go_left = col > 0
        can_go_right = col < grid_width - 1

        if can_go_up:
            next_nodes.append((row - 1, col))
        if can_go_down:
            next_nodes.append((row + 1, col))
        if can_go_left:
            next_nodes.append((row, col - 1))
        if can_go_right:
            next_nodes.append((row, col + 1))
        return next_nodes

    def oranges_rotting(self, grid: list[list[int]]):
        # pylint: disable=no-self-use
        """
        In a given grid, each cell can have one of three values:

        the value 0 representing an empty cell;
        the value 1 representing a fresh orange;
        the value 2 representing a rotten orange.
        Every minute, any fresh orange that is adjacent (4-directionally)
        to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange.
          If this is impossible, return -1 instead.
        """
        if len(grid) == 0:
            return 0

        # find out all initial rotten orange and
        # for each minutes elapsed, propagate the rotten status
        grid_height = len(grid)
        grid_width = len(grid[0])
        # Use BFS to start level-wise exploration from all initial rotten orange
        visited: set[tuple[int, int]] = set()
        # with a queue of tuples (row, col, minute_took)
        queue: deque[tuple[int, int]] = deque()
        num_fresh_orange = 0

        for row in range(grid_height):
            for col in range(grid_width):
                if (
                    grid[row][col] == 2
                ):  # Add the initial rotten orange to the BFS queue
                    queue.append((row, col))
                if grid[row][col] == 1:  # initialize the fresh orange counter
                    num_fresh_orange += 1

        # if there are no fresh orange in the initial setup, return 0
        if num_fresh_orange == 0:
            return 0

        total_minute_took = -1  # at time = 0, the queue items are already rotten.
        while queue:
            next_queue: deque[tuple[int, int]] = deque()
            while queue:
                row, col = queue.popleft()
                # filter all possible next moves
                next_nodes = self.next_moves(row, col, grid_width, grid_height)
                for nrow, ncol in next_nodes:
                    # check visited or not
                    if (nrow, ncol) in visited:
                        continue
                    visited.add((nrow, ncol))
                    # Only move to fresh orange
                    if grid[nrow][ncol] == 1:
                        num_fresh_orange -= 1
                        next_queue.append((nrow, ncol))

            total_minute_took += 1
            queue = next_queue

        if num_fresh_orange == 0:  # If at the end all orange are rotten
            return total_minute_took
        return -1
