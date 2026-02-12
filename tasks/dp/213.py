# Difficulty: Medium
# https://leetcode.com/problems/house-robber-ii
# Time - O(n), Space - O(1)

from typing import List


class Solution:
    def _rob_linear(self, nums: List[int]) -> int:
        # Look two houses back to decide whether to rob the current house or not
        prev, curr = 0, 0
        for x in nums:
            # Update the maximum amount that can be robbed up to the current house
            prev, curr = curr, max(curr, prev + x)
        return curr

    def rob(self, nums: List[int]) -> int:
        # Handle edge case where there's only one house
        if len(nums) == 1:
            return nums[0]
        # Since the houses are in a circle, we can't rob both the first and last house at the same time
        return max(
            self._rob_linear(nums[:-1]),
            self._rob_linear(nums[1:])
        )
