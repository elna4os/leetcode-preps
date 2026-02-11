# Difficulty: Medium
# https://leetcode.com/problems/maximum-strength-of-a-group
# Time - O(n), Space - O(1)

from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Initialize maximum and minimum products
        mx = mn = nums[0]
        for x in nums[1:]:
            # Update maximum and minimum products considering the current number
            mx, mn = max(mx, mx * x, mn * x, x), min(mn, mn * x, mx * x, x)

        return mx
