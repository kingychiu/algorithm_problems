"""
    https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
from typing import List, Tuple, Optional

from src.data_structures.leetcode.tree import Node


class Solution:
    # pylint: disable=too-few-public-methods
    """
    Solution
    """

    def max_depth(self, root: Optional[Node]) -> int:
        # pylint: disable=no-self-use
        """
        Return the max depth of the given N-ary Tree
        """
        if not root:
            return 0

        # Setting up a queue for BFS with item = (node, node_level)
        queue: List[Tuple[Node, int]] = [(root, 1)]
        max_level: int = 1
        while queue:
            # de-queue
            curr_node, curr_level = queue.pop(0)
            # update maximum level
            max_level = max(curr_level, max_level)

            if curr_node.children is not None:
                for child in curr_node.children:
                    # en-queue the child node and add 1 to the level
                    queue.append((child, curr_level + 1))
        return max_level
