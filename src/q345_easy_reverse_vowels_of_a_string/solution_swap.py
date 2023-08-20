#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}  # noqa: RUF012

    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        ptr1, ptr2 = 0, len(s) - 1
        while ptr1 < ptr2:
            if lst[ptr1] not in self.vowels:
                ptr1 += 1
            elif lst[ptr2] not in self.vowels:
                ptr2 -= 1
            else:
                print("swap")
                lst[ptr1], lst[ptr2] = lst[ptr2], lst[ptr1]
                ptr1 += 1
                ptr2 -= 1
        return "".join(lst)


# @lc code=end
