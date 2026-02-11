# Difficulty: Medium
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n
# Time - O(n * m), Space - O(1) where n is the given number and m is the length of the string s

def has_substring(s: str, substring: str) -> bool:
    m, n = len(s), len(substring)
    if n > m:
        return False
    for i in range(m - n + 1):
        if s[i:i + n] == substring:
            return True
    return False


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            i_bin_str = bin(i)[2:]
            if not has_substring(s, i_bin_str):
                return False
        return True
