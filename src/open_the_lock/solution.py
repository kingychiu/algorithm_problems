"""
    https://leetcode.com/problems/open-the-lock/
"""


from collections import deque


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

    def next_moves(self, d1: int, d2: int, d3: int, d4: int) -> list[tuple[int, ...]]:
        # pylint: disable=no-self-use invalid-name too-many-arguments
        """
        It takes next moves from the current state.
        """
        next_moves: list[tuple[int, ...]] = []
        for idx, d in enumerate([d1, d2, d3, d4]):  # pylint: disable=invalid-name
            next_move = [d1, d2, d3, d4]
            next_move[idx] = self.next_digit(d, moving_up=True)
            next_moves.append(tuple(next_move))
            next_move = [d1, d2, d3, d4]
            next_move[idx] = self.next_digit(d, moving_up=False)
            next_moves.append(tuple(next_move))
        return next_moves

    def open_lock(self, deadends: list[str], target: str) -> int:
        # pylint: disable=no-self-use
        """
        Given a target representing the value of the wheels that will unlock the lock,
        return the minimum total number of turns required to open the lock,
        or -1 if it is impossible.
        """
        # hashmap for quick deadends lookup
        unique_deadends = set(deadends)

        # BFS queue (d1, d2, d3, d4, cost)
        queue: deque[tuple[int, ...]] = deque([(0, 0, 0, 0)])
        visited: set[str] = set()

        cost = 0
        while queue:
            next_queue: deque[tuple[int, ...]] = deque()
            while queue:
                d1, d2, d3, d4 = queue.popleft()  # pylint: disable=invalid-name
                d_str = f"{d1}{d2}{d3}{d4}"

                # Deadends
                if d_str in unique_deadends:
                    continue

                if d_str == target:
                    return cost

                # generate next possible moves
                next_moves = self.next_moves(d1, d2, d3, d4)

                for move in next_moves:
                    d_str = f"{move[0]}{move[1]}{move[2]}{move[3]}"
                    if d_str in visited:
                        continue
                    visited.add(d_str)
                    next_queue.append(move)

            queue = next_queue
            cost += 1

        return -1
