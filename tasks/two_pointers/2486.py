# Difficulty: Medium
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
# Time - O(n), Space - O(1), where n is the length of string s.

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        to_append = len(t)
        k = 0
        for i in range(len(s)):
            if k == len(t):
                break
            if s[i] == t[k]:
                k += 1
                to_append -= 1
        return to_append
