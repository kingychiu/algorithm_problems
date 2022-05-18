"""
    Tests for array representation of a binary tree
"""
import pytest
from src.data_structures.array_binary_tree import ArrayBinaryTree


@pytest.mark.parametrize(
    "height",
    [
        0,
        1,
        5,
        10,
        20,
    ],
)
def test_instantiation(height):
    """
    For a binary tree with height h, we need 2**h-1 length array.
    """
    tree = ArrayBinaryTree(height=height)
    assert len(tree.tree) == 2**height - 1


def test_tree_1():
    """
    Test value insertion
    """
    tree = ArrayBinaryTree(height=3)
    root_idx = tree.set_root(10)
    assert root_idx == 0
    idx = tree.set_left(root_idx, 9)
    assert idx == 1

    assert tree._get_parent_idx(idx) == root_idx  # pylint: disable=protected-access

    with pytest.raises(IndexError):
        tree.set_left(10, 1)


def test_tree_2():
    """
    Test value insertion
    """
    tree = ArrayBinaryTree(height=3)
    root_idx = tree.set_root("A")
    root_left_idx = tree.set_left(root_idx, "B")
    root_right_idx = tree.set_right(root_idx, "C")

    tree.set_left(root_left_idx, "D")
    tree.set_right(root_left_idx, "E")

    tree.set_left(root_right_idx, "F")

    levels = tree.print_tree()
    assert levels == [["A"], ["B", "C"], ["D", "E", "F", "None"]]
