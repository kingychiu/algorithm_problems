"""
    https://leetcode.com/problems/network-delay-time/
"""
from collections import defaultdict
import heapq


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def get_submission(self, times: list[list[int]], N: int, K: int) -> int:
        # pylint: disable=no-self-use
        """
        Now, we send a signal from a certain node K.
        How long will it take for all nodes to receive the signal?
        If it is impossible, return -1.
        """
        time_map: dict[int, dict[int, int]] = defaultdict(dict)
        for time in times:
            time_map[time[0]][time[1]] = time[2]

        q = [(0, K, 0)]
        heapq.heapify(q)
        visited = set()

        time_spent = 0
        while q:
            _, node, acc_time = heapq.heappop(q)
            if node not in visited:
                time_spent = max(time_spent, acc_time)
                visited.add(node)

            for nxt_node in time_map[node].keys():
                if nxt_node not in visited:
                    nxt_time = time_map[node][nxt_node]
                    heapq.heappush(
                        q, (acc_time + nxt_time, nxt_node, acc_time + nxt_time)
                    )

        if len(visited) == N:
            return time_spent
        return -1
