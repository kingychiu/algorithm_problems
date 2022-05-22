"""
    Tests for a binary search tree
"""
from src.data_structures import binary_search_tree


def test_tree_traversal():
    """
    Test Binary Search Tree
               8
             /   \
            /     \
           3       10
          / \       \
         /   \       \
        1     6       14
             / \     /
            /   \   /
           4     7 13
    """

    root = binary_search_tree.BinarySearchTreeNode(8)
    root.left = binary_search_tree.BinarySearchTreeNode(3)
    root.left.left = binary_search_tree.BinarySearchTreeNode(1)
    root.left.right = binary_search_tree.BinarySearchTreeNode(6)
    root.left.right.left = binary_search_tree.BinarySearchTreeNode(4)
    root.left.right.right = binary_search_tree.BinarySearchTreeNode(7)

    root.right = binary_search_tree.BinarySearchTreeNode(10)
    root.right.right = binary_search_tree.BinarySearchTreeNode(14)
    root.right.right.left = binary_search_tree.BinarySearchTreeNode(13)

    results_recursive = binary_search_tree.inorder_recursive(root)
    results_iterative = binary_search_tree.inorder_iterative(root)

    for results in [results_recursive, results_iterative]:
        assert [result[0] for result in results] == [1, 3, 4, 6, 7, 8, 10, 13, 14]
        assert [result[1] for result in results] == [1] * len(results)

    results_recursive = binary_search_tree.preorder_recursive(root)
    results_iterative = binary_search_tree.preorder_iterative(root)

    for results in [results_recursive, results_iterative]:
        assert [result[0] for result in results] == [8, 3, 1, 6, 4, 7, 10, 14, 13]
        assert [result[1] for result in results] == [1] * len(results)

    results_recursive = binary_search_tree.postorder_recursive(root)

    for results in [results_recursive]:
        assert [result[0] for result in results] == [1, 4, 7, 6, 3, 13, 14, 10, 8]
        assert [result[1] for result in results] == [1] * len(results)

    results = binary_search_tree.levelorder(root)
    assert [result[0] for result in results] == [8, 3, 10, 1, 6, 14, 4, 7, 13]
    assert [result[1] for result in results] == [1] * len(results)


def test_tree_insert_recursive():
    """
    Test Binary Search Tree
               8
             /   \
            /     \
           3       10
          / \       \
         /   \       \
        1     6       14
             / \     /
            /   \   /
           4     7 13
    """

    root = binary_search_tree.BinarySearchTreeNode(8)
    root.left = binary_search_tree.BinarySearchTreeNode(3)
    root.left.left = binary_search_tree.BinarySearchTreeNode(1)
    root.left.right = binary_search_tree.BinarySearchTreeNode(6)
    root.left.right.left = binary_search_tree.BinarySearchTreeNode(4)
    root.left.right.right = binary_search_tree.BinarySearchTreeNode(7)

    root.right = binary_search_tree.BinarySearchTreeNode(10)
    root.right.right = binary_search_tree.BinarySearchTreeNode(14)
    root.right.right.left = binary_search_tree.BinarySearchTreeNode(13)

    binary_search_tree.insert_recursive(root, 0)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 10, 13, 14]

    binary_search_tree.insert_recursive(root, 9)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 14]

    binary_search_tree.insert_recursive(root, 1)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 14]
    assert root.left.left.count == 2

    binary_search_tree.insert_recursive(root, 15)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 14, 15]
    assert root.left.left.count == 2

    root = binary_search_tree.insert_recursive(None, 0)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0]


def test_tree_insert_iterative():
    """
    Test Binary Search Tree
               8
             /   \
            /     \
           3       10
          / \       \
         /   \       \
        1     6       14
             / \     /
            /   \   /
           4     7 13
    """

    root = binary_search_tree.BinarySearchTreeNode(8)
    root.left = binary_search_tree.BinarySearchTreeNode(3)
    root.left.left = binary_search_tree.BinarySearchTreeNode(1)
    root.left.right = binary_search_tree.BinarySearchTreeNode(6)
    root.left.right.left = binary_search_tree.BinarySearchTreeNode(4)
    root.left.right.right = binary_search_tree.BinarySearchTreeNode(7)

    root.right = binary_search_tree.BinarySearchTreeNode(10)
    root.right.right = binary_search_tree.BinarySearchTreeNode(14)
    root.right.right.left = binary_search_tree.BinarySearchTreeNode(13)

    binary_search_tree.insert_iterative(root, 0)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 10, 13, 14]

    binary_search_tree.insert_iterative(root, 9)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 14]

    binary_search_tree.insert_iterative(root, 1)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 14]
    assert root.left.left.count == 2

    binary_search_tree.insert_iterative(root, 15)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0, 1, 3, 4, 6, 7, 8, 9, 10, 13, 14, 15]
    assert root.left.left.count == 2

    root = binary_search_tree.insert_iterative(None, 0)
    results = binary_search_tree.inorder_recursive(root)
    assert [result[0] for result in results] == [0]
