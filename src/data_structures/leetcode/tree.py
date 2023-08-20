"""
    Classes and helper functions for tree-like data structures on leetcode
"""
from typing import Generic, Optional

from src.common import TemplateType


class Node(Generic[TemplateType]):  # pylint: disable=too-few-public-methods
    """
    A Node for N-ary Tree
    """

    def __init__(
        self,
        val: TemplateType,
        children: Optional[list["Node"]] = None,
    ):
        self.val: TemplateType = val
        self.children: Optional[list["Node"]] = children


class TreeNode(Generic[TemplateType]):  # pylint: disable=too-few-public-methods
    """
    A Node for Binary Tree.
    """

    def __init__(self, val: TemplateType):
        self.val: TemplateType = val
        self.left: Optional[TreeNode[TemplateType]] = None
        self.right: Optional[TreeNode[TemplateType]] = None


def parse_list_to_n_ary_tree(values: list[TemplateType]) -> Optional[Node]:
    """
    It takes an array of value and convert them into a N-ary tree
    """
    if not values:
        return None

    root = Node(values[0])
    parent_queue = [root]
    curr_parent: Optional[Node[TemplateType]] = None
    for idx in range(1, len(values)):
        value = values[idx]
        if value is None:
            curr_parent = parent_queue.pop(0)
        elif curr_parent:
            node = Node(value)
            parent_queue.append(node)
            if curr_parent.children:
                curr_parent.children.append(node)
            else:
                curr_parent.children = [node]
    return root


def parse_list_to_binary_tree(values: list[TemplateType]) -> Optional[TreeNode]:
    """
    It takes an array of value and convert them into a binary tree
    """
    if not values:
        return None

    root = TreeNode(values[0])
    parent_queue = [(root, "L"), (root, "R")]
    for idx in range(1, len(values)):
        value = values[idx]
        curr_parent = parent_queue.pop(0)
        if value is not None:
            node = TreeNode(value)
            parent_queue.append((node, "L"))
            parent_queue.append((node, "R"))
            if curr_parent[1] == "L":
                curr_parent[0].left = node
            elif curr_parent[1] == "R":
                curr_parent[0].right = node
    return root
