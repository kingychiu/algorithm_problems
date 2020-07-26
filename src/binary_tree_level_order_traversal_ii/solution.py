"""
    https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""
from typing import List, Optional, Tuple

from src.data_structures.leetcode.tree import Node, TreeNode


class Solution:
    # pylint: disable=too-few-public-methods
    """
        Solution
    """

    def level_order_bottom(self, root: Optional[Node]) -> List[List[int]]:
        # pylint: disable=no-self-use
        """
            Given a binary tree, return the bottom-up level order traversal of its nodes' values.
            (ie, from left to right, level by level from leaf to root).
        """
        results = []
        if not root:
            return results

        # bfs
        queue: List[Tuple[TreeNode, int]] = [(root, 1)]
        max_level = 0
        results = []
        while len(queue) > 0:
            node, level = queue[0]
            if level > max_level:
                max_level = level
                # switch level
                results.append([p_node.val for p_node, p_level in queue])

            queue.pop(0)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return list(reversed(results))
