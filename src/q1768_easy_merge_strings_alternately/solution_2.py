#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        result_str = []
        for idx in range(min_len):
            result_str.append(word1[idx])
            result_str.append(word2[idx])

        if len1 > len2:
            for idx in range(len2, len1):
                result_str.append(word1[idx])
        elif len2 > len1:
            for idx in range(len1, len2):
                result_str.append(word2[idx])

        return "".join(result_str)


# @lc code=end
