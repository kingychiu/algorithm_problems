""" Testing solution """

import pytest

from src.data_structures.leetcode.tree import parse_list_to_n_ary_tree
from src.n_ary_tree_level_order_traversal.solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([], []),
        ([1, None, 3, 2, 4, None, 5, 6], [[1], [3, 2, 4], [5, 6]])
    ],
)
def test_solution(test_input, expected):
    """
        Checking Test Cases
    """
    root = parse_list_to_n_ary_tree(test_input)
    assert Solution().level_order(root) == expected
