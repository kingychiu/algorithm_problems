"""
    https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""
from typing import Optional
from collections import deque
from src.data_structures.leetcode.tree import TreeNode


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def level_order_bottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        # pylint: disable=no-self-use
        """
        Given a binary tree, return the bottom-up level order traversal of its nodes' values.
        (ie, from left to right, level by level from leaf to root).
        """
        results: list[list[int]] = []
        if not root:
            return results

        # bfs
        queue: deque[TreeNode] = deque([root])

        results = []
        while queue:
            level_results: list[int] = []
            next_queue: deque[TreeNode] = deque()
            while queue:
                node = queue.popleft()
                level_results.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            results.append(level_results)
            queue = next_queue
        return list(reversed(results))
