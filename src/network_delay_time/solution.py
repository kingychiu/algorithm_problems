"""
    https://leetcode.com/problems/network-delay-time/
"""
from collections import defaultdict
from queue import PriorityQueue
from typing import List


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def get_submission(self, times: List[List[int]], N: int, K: int) -> int:
        # pylint: disable=no-self-use
        """
        Now, we send a signal from a certain node K.
        How long will it take for all nodes to receive the signal?
        If it is impossible, return -1.
        """
        time_map = defaultdict(dict)
        for time in times:
            time_map[time[0]][time[1]] = time[2]

        q = PriorityQueue()
        q.put((0, K, 0))  # (priority, node_idx, accumulated_time)
        visited = set()

        time_spent = 0
        while not q.empty():
            _, node, acc_time = q.get()
            if node not in visited:
                time_spent = max(time_spent, acc_time)
                visited.add(node)

            for nxt_node in time_map[node].keys():
                if nxt_node not in visited:
                    nxt_time = time_map[node][nxt_node]
                    q.put((acc_time + nxt_time, nxt_node, acc_time + nxt_time))

        if len(visited) == N:
            return time_spent
        return -1
