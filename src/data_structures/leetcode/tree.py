"""
    Classes and helper functions for tree-like data structures on leetcode
"""
from typing import List, Generic, Optional

from src.common import TemplateType


class Node(Generic[TemplateType]):  # pylint: disable=too-few-public-methods
    """
        A Node class is the basic building block for trees.
    """

    def __init__(self,
                 val: Optional[TemplateType] = None,
                 children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children


def parse_list_to_tree(values: List[TemplateType]) -> Optional[Node]:
    """
        It takes an array of value and convert them into a tree
    """
    if not values:
        return None

    root = Node(values[0])
    parent_queue = [root]

    curr_parent = None
    for idx in range(1, len(values)):
        value = values[idx]
        if value is None:
            curr_parent = parent_queue.pop(0)
        else:
            node = Node(value)
            parent_queue.append(node)
            if curr_parent.children:
                curr_parent.children.append(node)
            else:
                curr_parent.children = [node]
    return root
