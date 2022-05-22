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
    It is helpful when we want to clone a BST,
    Create a new BST B by inserting the results from preorder traversing BST A
    """
    results = []

    # Call stack for back tracking
    # We need a stack here, because there is more than 1 "previous"
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


def smallest_recursive(node: BinarySearchTreeNode):
    """
    Get the smallest (left-most) value
    """
    # Base case
    if node.left is None:
        return node
    return smallest_recursive(node.left)


def largest_recursive(node: BinarySearchTreeNode):
    """
    Get the largest (right-most) value
    """
    # Base case
    if node.right is None:
        return node
    return largest_recursive(node.right)


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


def insert_iterative(root: Optional[BinarySearchTreeNode], val: int):
    """Standard BST Insertion"""
    # Left Value < Root Value < Right Vale
    if root is None:
        return BinarySearchTreeNode(val)

    curr = root
    while curr is not None:
        # Compare the value with the root value
        if curr.val == val:  # Increment the counter
            curr.count += 1
            return curr

        if val < curr.val:  # Go left
            if curr.left is not None:
                curr = curr.left
            else:
                curr.left = BinarySearchTreeNode(val)
                return curr.left
        else:  # Go right
            if curr.right:
                curr = curr.right
            else:
                curr.right = BinarySearchTreeNode(val)
                return curr.right


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
    right_smallest_node = smallest_recursive(root.right)
    # If we found the smallest right node
    delete_recursive(root.right, right_smallest_node.val)
    # Replace with the smallest node
    right_smallest_node.right = (
        root.right if root.right.val != right_smallest_node.val else None
    )
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
