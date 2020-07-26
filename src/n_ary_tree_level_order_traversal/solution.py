"""
    https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
from typing import Optional, List, Tuple

from src.data_structures.leetcode.tree import Node


class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    def level_order(self, root: Optional[Node] = None) -> List[List[int]]:
        # pylint: disable=no-self-use
        """
            Given an n-ary tree, return the level order traversal of its nodes' values.
        """
        if root is None:
            return []

        # BFS with a queue of (Node, level)
        queue: List[Tuple[Node, int]] = []
        queue.append((root, 1))

        results = []
        current_result_len = 0

        while queue:
            current_node, current_level = queue.pop(0)
            if current_level > current_result_len:
                results.append([])
                current_result_len += 1

            results[current_level - 1].append(current_node.val)
            if current_node.children:
                for child in current_node.children:
                    queue.append((child, current_level + 1))

        return results
