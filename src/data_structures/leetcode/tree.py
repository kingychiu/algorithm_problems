"""
    Classes and helper functions for tree-like data structures on leetcode
"""
from typing import List, Generic, Optional

from common import TemplateType


class Node(Generic[TemplateType]):  # pylint: disable=too-few-public-methods
    """
        A Node for N-ary Tree
    """

    def __init__(self,
                 val: Optional[TemplateType] = None,
                 children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children


class TreeNode(Generic[TemplateType]):  # pylint: disable=too-few-public-methods
    """
        A Node for Binary Tree.
    """

    def __init__(self, val: Optional[TemplateType] = None):
        self.val = val
        self.left = None
        self.right = None


def parse_list_to_n_ary_tree(values: List[TemplateType]) -> Optional[Node]:
    """
        It takes an array of value and convert them into a N-ary tree
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


def parse_list_to_binary_tree(values: List[TemplateType]) -> Optional[TreeNode]:
    """
            It takes an array of value and convert them into a binary tree
    """
    if not values:
        return None

    root = TreeNode(values[0])
    parent_queue = [(root, 'L'), (root, 'R')]
    for idx in range(1, len(values)):
        value = values[idx]
        curr_parent = parent_queue.pop(0)
        if value is not None:
            node = TreeNode(value)
            parent_queue.append((node, 'L'))
            parent_queue.append((node, 'R'))
            if curr_parent[1] == 'L':
                curr_parent[0].left = node
            elif curr_parent[1] == 'R':
                curr_parent[0].right = node
    return root
