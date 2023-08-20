"""
    https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
from collections import deque
from typing import Optional

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
        queue: deque[Node] = deque([root])
        max_level: int = 0
        while queue:
            next_queue: deque[Node] = deque()
            while queue:
                # de-queue
                curr_node = queue.popleft()
                if curr_node.children is not None:
                    for child in curr_node.children:
                        # en-queue the child node and add 1 to the level
                        next_queue.append(child)
            # update maximum level
            max_level += 1
            queue = next_queue

        return max_level
