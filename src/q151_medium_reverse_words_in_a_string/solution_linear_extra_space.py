#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        lst = [w.strip() for w in s.split(" ")]
        lst = [w for w in lst if w]
        return " ".join(lst[::-1])


# @lc code=end
