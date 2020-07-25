"""
    Tests for tree-like data structures.
"""

from src.data_structures.leetcode.tree import Node, parse_list_to_tree


def test_node():
    """
        Test Node Class
    """
    node = Node(1)
    assert node.val == 1
    assert node.children is None


def test_n_ary_tree():
    """
        Test Node Class with children
    """
    root = Node(1,
                children=[
                    Node(2),
                    Node(4, children=[Node(1)])
                ])
    assert root.val == 1
    assert root.children is not None
    assert root.children[0].val == 2
    assert root.children[0].children is None
    assert root.children[1].val == 4
    assert root.children[1].children[0].val == 1
    assert root.children[1].children[0].children is None


def test_parse_list_to_tree():
    """
        Test parse_list_to_tree
    """
    assert parse_list_to_tree([]) is None

    input1 = [1]
    root = parse_list_to_tree(input1)
    assert root.val == 1
    assert root.children is None

    input2 = [1, None]
    root = parse_list_to_tree(input2)
    assert root.val == 1
    assert root.children is None

    input3 = [1, None, 2, 3, 4]
    root = parse_list_to_tree(input3)
    assert root.val == 1
    assert root.children[0].val == 2
    assert root.children[0].children is None
    assert root.children[1].val == 3
    assert root.children[1].children is None
    assert root.children[2].val == 4
    assert root.children[2].children is None

    input4 = [1, None, 3, None, 5]
    root = parse_list_to_tree(input4)
    assert root.val == 1
    assert root.children[0].val == 3
    assert root.children[0].children[0].val == 5
    assert root.children[0].children[0].children is None

    input5 = [1, None, 2, 3, 4, 5, None, None, 6, 7,
              None, 8, None, 9, 10]
    root = parse_list_to_tree(input5)
    assert root.val == 1
    assert [child.val for child in root.children] == [2, 3, 4, 5]
    assert root.children[0].children is None
    assert [child.val for child in root.children[1].children] == [6, 7]
    assert [child.val for child in root.children[2].children] == [8]
    assert [child.val for child in root.children[3].children] == [9, 10]
