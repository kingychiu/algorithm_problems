#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
from collections import deque


# @lc code=start
class Solution:
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}  # noqa: RUF012

    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        size = len(lst)
        stack: deque[str] = deque([])
        vowel_indices = []
        # Put vowels in stack
        for idx in range(size):
            if lst[idx] in self.vowels:
                stack.append(lst[idx])
                vowel_indices.append(idx)

        # Reverse only the vowel indices
        for idx in vowel_indices:
            lst[idx] = stack.pop()

        return "".join(lst)


# @lc code=end
