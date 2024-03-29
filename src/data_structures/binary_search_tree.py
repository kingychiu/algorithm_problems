"""Binary Search Tree"""
from collections import deque
from typing import Optional


class BinarySearchTreeNode:  # pylint: disable=too-few-public-methods
    """
    A Node for Binary Tree.
    """

    def __init__(self, val: int):
        self.val: int = val
        self.count: int = 1
        self.left: Optional[BinarySearchTreeNode] = None
        self.right: Optional[BinarySearchTreeNode] = None


def inorder_recursive(node: Optional[BinarySearchTreeNode]):
    """
    (Left, Node, Right)
    It is helpful when we want to print out the BST values in order
    """
    # Base case
    if node is None:
        return []

    results = []
    # Left
    results += inorder_recursive(node.left)
    # Node
    results.append((node.val, node.count))
    # Right
    results += inorder_recursive(node.right)
    return results


def preorder_recursive(node: Optional[BinarySearchTreeNode]):
    """
    (Root, Left, Right)
    It is helpful when we want to clone a BST,
    Create a new BST B by inserting the results from preorder traversing BST A
    """
    # Base case
    if node is None:
        return []

    results = []
    # Node
    results.append((node.val, node.count))
    # Left
    results += preorder_recursive(node.left)
    # Right
    results += preorder_recursive(node.right)
    return results


def postorder_recursive(node: Optional[BinarySearchTreeNode]):
    """
    (Left, Right, Root)
    """
    # Base case
    if node is None:
        return []

    results = []
    # Left
    results += postorder_recursive(node.left)
    # Right
    results += postorder_recursive(node.right)
    # Node
    results.append((node.val, node.count))
    return results


def inorder_iterative(node: BinarySearchTreeNode):
    """
    (Left, Node, Right)
    It is helpful when we want to print out the BST values in order
    """
    results = []

    # Call stack for back tracking,
    # We need a stack here, because there is more than 1 "previous"
    stack: deque = deque()

    # Dive to the left most
    def _dive(leftmost: Optional[BinarySearchTreeNode]):
        while leftmost is not None:
            stack.append(leftmost)
            leftmost = leftmost.left

    _dive(node)

    while stack:
        curr = stack.pop()
        results.append((curr.val, curr.count))
        # Left most child of the right subtree
        _dive(curr.right)

    return results


def preorder_iterative(node: BinarySearchTreeNode):
    """
    (Node, Left, Right)
    It is helpful when we want to clone a BST,
    Create a new BST B by inserting the results from preorder traversing BST A
    """
    results = []

    # Call stack for back tracking,
    # We need a stack here, because there is more than 1 "previous"
    stack: deque = deque()

    # Dive to the left most
    def _dive(leftmost: Optional[BinarySearchTreeNode]):
        while leftmost is not None:
            results.append((leftmost.val, leftmost.count))
            stack.append(leftmost)
            leftmost = leftmost.left

    _dive(node)

    while stack:
        curr = stack.pop()
        # Left most child of the right subtree
        _dive(curr.right)

    return results


def levelorder(node: BinarySearchTreeNode):
    """
    BFS
    """
    q: deque = deque()
    # Root level
    q.append(node)
    results = [(node.val, node.count)]

    while q:
        curr_node = q.popleft()
        if curr_node.left:
            results.append((curr_node.left.val, curr_node.left.count))
            q.append(curr_node.left)

        if curr_node.right:
            results.append((curr_node.right.val, curr_node.right.count))
            q.append(curr_node.right)
    return results


def smallest(node: BinarySearchTreeNode) -> BinarySearchTreeNode:
    """
    Get the smallest (left-most) value
    """
    curr = node
    while curr.left:
        curr = curr.left
    return curr


def largest(node: BinarySearchTreeNode) -> BinarySearchTreeNode:
    """
    Get the largest (right-most) value
    """
    curr = node
    while curr.right:
        curr = curr.right
    return curr


def search(
    node: Optional[BinarySearchTreeNode], val: int
) -> Optional[BinarySearchTreeNode]:
    """
    Get the node containing the target val
    """
    curr = node
    while curr:
        if val == curr.val:
            return curr
        curr = curr.left if val < curr.val else curr.right

    return None


def insert_recursive(root: Optional[BinarySearchTreeNode], val: int):
    """Standard BST Insertion"""
    # Left Value < Root Value < Right Vale
    if root is None:
        return BinarySearchTreeNode(val)

    if root.val == val:
        root.count += 1
    elif val < root.val:
        root.left = insert_recursive(root.left, val)
    else:
        root.right = insert_recursive(root.right, val)
    return root


def insert_iterative(
    root: Optional[BinarySearchTreeNode], val: int
) -> BinarySearchTreeNode:
    """Standard BST Insertion"""
    # Left Value < Root Value < Right Vale
    if root is None:
        return BinarySearchTreeNode(val)

    curr = root
    while curr is not None:
        # Compare the value with the root value
        if curr.val == val:  # Increment the counter
            curr.count += 1
            break

        if val < curr.val:  # Go left
            if curr.left is not None:
                curr = curr.left
            else:
                curr.left = BinarySearchTreeNode(val)
                break
        else:  # Go right
            if curr.right:
                curr = curr.right
            else:
                curr.right = BinarySearchTreeNode(val)
                break
    return root


def delete_recursive(root: Optional[BinarySearchTreeNode], val: int):
    """Standard BST Deletion"""

    # Base case
    if root is None:  # Value not found
        raise ValueError

    # Left Value < Root Value < Right Vale
    if val < root.val:
        root.left = delete_recursive(root.left, val)
        return root
    if val > root.val:
        root.right = delete_recursive(root.right, val)
        return root
    # Reduce Count
    if root.count > 1:
        root.count -= 1
        return root

    if root.right is None:
        # If the right sub tree is empty, replace with the left sub tree
        return root.left

    # Imagine we have [1, 2, 3, 4, 5]
    # if we want to delete 3, we need shifting 4, and 5
    # Locate the smallest right node
    right_smallest_node = smallest(root.right)
    # Replace the node with the smallest node
    # The new right subtree should not contain the smallest value
    right_smallest_node.right = delete_recursive(root.right, right_smallest_node.val)
    # Replace with the smallest node
    right_smallest_node.left = root.left
    return right_smallest_node


# def avl_insert(root: BinarySearchTreeNode, val: int):
#     """
#     AVL tree is a self-balancing Binary Search Tree (BST) where the difference between
#     heights of left and right subtrees cannot be more than one for all nodes.
#     """
#     # node_w = insert(root, val)


# def avl_delete():
#     """
#     AVL tree is a self-balancing Binary Search Tree (BST) where the difference between
#     heights of left and right subtrees cannot be more than one for all nodes.
#     """
