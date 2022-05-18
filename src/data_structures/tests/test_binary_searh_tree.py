"""
    Tests for a binary search tree
"""
from src.data_structures import binary_search_tree


def test_tree_1():
    """
    Test Binary Search Tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    """

    root = binary_search_tree.BinarySearchTreeNode(1)
    root.left = binary_search_tree.BinarySearchTreeNode(2)
    root.left.left = binary_search_tree.BinarySearchTreeNode(4)

    root.right = binary_search_tree.BinarySearchTreeNode(3)
    root.right.right = binary_search_tree.BinarySearchTreeNode(6)
    root.right.left = binary_search_tree.BinarySearchTreeNode(5)
    root.right.left.left = binary_search_tree.BinarySearchTreeNode(7)
    root.right.left.right = binary_search_tree.BinarySearchTreeNode(8)

    results_recursive = binary_search_tree.inorder_recursive(root)
    results_iterative = binary_search_tree.inorder_iterative(root)

    for results in [results_recursive, results_iterative]:
        assert [result[0] for result in results] == [4, 2, 1, 7, 5, 8, 3, 6]
        assert [result[1] for result in results] == [1] * len(results)

    results_recursive = binary_search_tree.preorder_recursive(root)
    results_iterative = binary_search_tree.preorder_iterative(root)

    for results in [results_recursive, results_iterative]:
        assert [result[0] for result in results] == [1, 2, 4, 3, 5, 7, 8, 6]
        assert [result[1] for result in results] == [1] * len(results)

    results_recursive = binary_search_tree.postorder_recursive(root)

    for results in [results_recursive]:
        assert [result[0] for result in results] == [4, 2, 7, 8, 5, 6, 3, 1]
        assert [result[1] for result in results] == [1] * len(results)

    results = binary_search_tree.levelorder(root)
    assert [result[0] for result in results] == [1, 2, 3, 4, 5, 6, 7, 8]
    assert [result[1] for result in results] == [1] * len(results)
