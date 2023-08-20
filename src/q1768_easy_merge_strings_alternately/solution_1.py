#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        result_str = ""
        for idx in range(min(len1, len2)):
            result_str += word1[idx] + word2[idx]
        if len1 > len2:
            result_str += word1[len2:]
        elif len2 > len1:
            result_str += word2[len1:]
        return result_str


# @lc code=end
