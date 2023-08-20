""" Testing solution """

import pytest

from . import solution_1, solution_2

test_cases = [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
    ("", "", ""),
    ("", "pqr", "pqr"),
    ("abc", "", "abc"),
]


@pytest.mark.parametrize(
    "word1, word2, expected",
    test_cases,
)
def test_solution_1(word1, word2, expected):
    """
    Checking Test Cases
    """
    assert solution_1.Solution().mergeAlternately(word1, word2) == expected


@pytest.mark.parametrize(
    "word1, word2, expected",
    test_cases,
)
def test_solution_2(word1, word2, expected):
    """
    Checking Test Cases
    """
    assert solution_2.Solution().mergeAlternately(word1, word2) == expected
