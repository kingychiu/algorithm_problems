""" Testing solution """

import pytest

from .solution_linear_extra_space import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("a", "a"),
    ],
)
def test_solution(s, expected):
    """
    Checking Test Cases
    """
    assert Solution().reverseWords(s) == expected
