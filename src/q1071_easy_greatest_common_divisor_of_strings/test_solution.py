""" Testing solution """

import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "str1,str2,expected",
    [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
        ("ABCDEF", "ABC", ""),
        ("A", "A", "A"),
        ("A", "B", ""),
        ("AA", "A", "A"),
    ],
)
def test_solution(str1, str2, expected):
    """
    Checking Test Cases
    """
    assert Solution().gcdOfStrings(str1, str2) == expected
