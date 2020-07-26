""" Testing solution """

import pytest
from src.data_structures.leetcode.tree import parse_list_to_binary_tree
from src.binary_tree_level_order_traversal_ii.solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([], []),
        ([3, 9, 20, None, None, 15, 7], [
            [15, 7],
            [9, 20],
            [3]
        ])
    ],
)
def test_solution(test_input, expected):
    """
        Checking Test Cases
    """
    node = parse_list_to_binary_tree(test_input)
    assert Solution().level_order_bottom(node) == expected
