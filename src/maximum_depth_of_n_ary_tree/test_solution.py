""" Testing solution """

import pytest

from src.data_structures.leetcode.tree import parse_list_to_n_ary_tree
from src.maximum_depth_of_n_ary_tree.solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([], 0),
        ([1, None, 3, 2, 4, None, 5, 6], 3),
        (
            [
                1,
                None,
                2,
                3,
                4,
                5,
                None,
                None,
                6,
                7,
                None,
                8,
                None,
                9,
                10,
                None,
                None,
                11,
                None,
                12,
                None,
                13,
                None,
                None,
                14,
            ],
            5,
        ),
    ],
)
def test_solution(test_input, expected):
    """
    Checking Test Cases
    """
    node = parse_list_to_n_ary_tree(test_input)
    assert Solution().max_depth(node) == expected
