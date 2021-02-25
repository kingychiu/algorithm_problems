"""
    https://leetcode.com/problems/rotting-oranges/
"""
from typing import List, Tuple, Set


class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    def next_moves(self, row, col, grid_width, grid_height) -> List[Tuple[int, int]]:
        # pylint: disable=no-self-use
        """ Get next moves of the flooding"""
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

    def oranges_rotting(self, grid: List[List[int]]):
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
        visited: Set[int, int] = set()
        # with a queue of tuples (row, col, minute_took)
        queue: List[Tuple[int, int, int]] = []
        num_fresh_orange = 0

        for row in range(grid_height):
            for col in range(grid_width):
                if grid[row][col] == 2:  # Add the initial rotten orange to the BFS queue
                    queue.append((row, col, 0))
                if grid[row][col] == 1:  # initialize the fresh orange counter
                    num_fresh_orange += 1

        # if there are no fresh orange in the initial setup, return 0
        if num_fresh_orange == 0:
            return 0

        total_minute_took = 0
        while queue:
            # BFS dequeue
            row, col, minute_took = queue.pop(0)
            # update time
            total_minute_took = minute_took

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
                    # BFS enqueue
                    queue.append((nrow, ncol, minute_took + 1))

        if num_fresh_orange == 0:
            return total_minute_took
        return -1
