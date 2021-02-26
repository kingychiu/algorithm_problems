""" Testing solution """

import pytest

from src.minimum_window_substring.solution import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["ab", "b"], "b"),
        (["bbaa", "aba"], "baa"),
        (["aab", "aab"], "aab"),
        (["ADOBECODEBANC", "AB"], "BA"),
        (["ADOBECODEBANC", "ABC"], "BANC"),
        (["a", "a"], "a"),
        (["aa", "aa"], "aa"),
        (["abc", "abc"], "abc"),
        (["ADOBECODEBANC", "ADOBECODEBANC"], "ADOBECODEBANC"),
        (["", ""], ""),
    ],
)
def test_solution(test_input, expected):
    """
        Checking Test Cases
    """
    assert Solution().min_window(*test_input) == expected
