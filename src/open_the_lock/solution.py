"""
    https://leetcode.com/problems/open-the-lock/
"""
from typing import List, DefaultDict, Optional
from collections import defaultdict


class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    def next_digit(self, digit, moving_up=True) -> int:  # pylint: disable=invalid-name
        # pylint: disable=no-self-use
        """
            It takes a digit and return the next digit.
        """

        if moving_up and digit == 9:
            return 0
        if not moving_up and digit == 0:
            return 9

        return digit + 1 if moving_up else digit - 1

    def next_moves(self, d1, d2, d3, d4, cost) -> List[List[int]]:
        # pylint: disable=no-self-use invalid-name too-many-arguments
        """
            It takes next moves from the current state.
        """
        next_moves = []
        for idx, d in enumerate([d1, d2, d3, d4]):  # pylint: disable=invalid-name
            next_move = [d1, d2, d3, d4, cost + 1]
            next_move[idx] = self.next_digit(d, moving_up=True)
            next_moves.append(next_move)
            next_move = [d1, d2, d3, d4, cost + 1]
            next_move[idx] = self.next_digit(d, moving_up=False)
            next_moves.append(next_move)
        return next_moves

    def open_lock(self, deadends: List[str], target: str) -> int:
        # pylint: disable=no-self-use
        """
            Given a target representing the value of the wheels that will unlock the lock,
            return the minimum total number of turns required to open the lock,
            or -1 if it is impossible.
        """
        # hashmap for quick deadends lookup
        deadends_dict: DefaultDict[str, bool] = defaultdict(lambda: False)
        for deadend in deadends:
            deadends_dict[deadend] = True

        # BFS queue (d1, d2, d3, d4, cost)
        queue: List[List[int, int, int, int, int]] = [[0, 0, 0, 0, 0]]
        visited: DefaultDict[str, bool] = defaultdict(lambda: False)

        while queue:
            # BFS dequeue
            d1, d2, d3, d4, cost = queue.pop(0)  # pylint: disable=invalid-name

            # Construct a state key
            d_str = f'{d1}{d2}{d3}{d4}'
            if deadends_dict[d_str]:
                continue

            # if target found
            if d_str == target:
                return cost

            # generate next possible moves
            next_moves = self.next_moves(d1, d2, d3, d4, cost)

            for move in next_moves:
                d_str = f'{move[0]}{move[1]}{move[2]}{move[3]}'
                if visited[d_str]:
                    continue
                visited[d_str] = True
                queue.append(move)
        return -1
