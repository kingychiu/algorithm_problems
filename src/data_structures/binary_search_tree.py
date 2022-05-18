"""Binary Search Tree"""
from typing import Optional
from queue import Queue, LifoQueue


class BinarySearchTreeNode:  # pylint: disable=too-few-public-methods
    """
    A Node for Binary Tree.
    """

    def __init__(self, val: int):
        self.val: int = val
        self.count: int = 1
        self.left: Optional[BinarySearchTreeNode] = None
        self.right: Optional[BinarySearchTreeNode] = None


def inorder_recursive(node: BinarySearchTreeNode):
    """
    (Left, Node, Right)
    """
    results = []
    # Left
    if node.left:
        results += inorder_recursive(node.left)
    # Node
    results.append((node.val, node.count))
    # Right
    if node.right:
        results += inorder_recursive(node.right)
    return results


def preorder_recursive(node: BinarySearchTreeNode):
    """
    (Root, Left, Right)
    """
    results = []
    # Node
    results.append((node.val, node.count))
    # Left
    if node.left:
        results += preorder_recursive(node.left)
    # Right
    if node.right:
        results += preorder_recursive(node.right)
    return results


def postorder_recursive(node: BinarySearchTreeNode):
    """
    (Left, Right, Root)
    """
    results = []
    # Left
    if node.left:
        results += postorder_recursive(node.left)
    # Right
    if node.right:
        results += postorder_recursive(node.right)
    # Node
    results.append((node.val, node.count))
    return results


def inorder_iterative(node: BinarySearchTreeNode):
    """
    (Left, Node, Right)
    """
    results = []

    # Call stack for back tracking
    stack: LifoQueue = LifoQueue()
    curr: Optional[BinarySearchTreeNode] = node
    while not stack.empty() or curr:
        if curr:
            # Keep going Left
            stack.put(curr)
            curr = curr.left
        else:
            # Back Track to Node
            curr = stack.get()
            results.append((curr.val, curr.count))  # type: ignore
            # Visit Right
            curr = curr.right  # type: ignore
    return results


def preorder_iterative(node: BinarySearchTreeNode):
    """
    (Node, Left, Right)
    """
    results = []

    # Call stack for back tracking
    stack: LifoQueue = LifoQueue()
    curr: Optional[BinarySearchTreeNode] = node
    while not stack.empty() or curr:
        if curr:
            results.append((curr.val, curr.count))  # type: ignore
            # Keep going Left
            stack.put(curr)
            curr = curr.left
        else:
            # Back Track to Node
            curr = stack.get()
            # Visit Right
            curr = curr.right  # type: ignore
    return results


def levelorder(node: BinarySearchTreeNode):
    """
    BFS
    """
    q: Queue = Queue()
    # Root level
    q.put(node)
    results = [(node.val, node.count)]

    while not q.empty():
        curr_node = q.get()
        if curr_node.left:
            results.append((curr_node.left.val, curr_node.left.count))
            q.put(curr_node.left)

        if curr_node.right:
            results.append((curr_node.right.val, curr_node.right.count))
            q.put(curr_node.right)
    return results
