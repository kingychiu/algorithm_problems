""" Testing solution """

import pytest

from .solution_stack import Solution as SolutionStack
from .solution_swap import Solution as SolutionSwap


@pytest.mark.parametrize(
    "s,expected",
    [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("ae", "ea"),
        ("ak", "ak"),
        ("a", "a"),
        ("kaej", "keaj"),
        ("kaoej", "keoaj"),
        ("aAaA", "AaAa"),
    ],
)
def test_solution(s, expected):
    """
    Checking Test Cases
    """
    assert SolutionSwap().reverseVowels(s) == expected
    assert SolutionStack().reverseVowels(s) == expected
