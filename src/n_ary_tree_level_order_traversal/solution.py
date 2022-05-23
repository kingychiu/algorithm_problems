"""
    https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
from typing import Optional
from collections import deque

from src.data_structures.leetcode.tree import Node


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def level_order(self, root: Optional[Node] = None) -> list[list[int]]:
        # pylint: disable=no-self-use
        """
        Given an n-ary tree, return the level order traversal of its nodes' values.
        """
        if root is None:
            return []

        # BFS with a queue of (Node, level)
        queue: deque[Node] = deque([root])

        results: list[list[int]] = []

        while queue:
            level_results = []
            queue_next: deque[Node] = deque()
            while queue:
                node = queue.popleft()
                level_results.append(node.val)

                for next_node in node.children or []:
                    queue_next.append(next_node)

            results.append(level_results)
            queue = queue_next

        return results
