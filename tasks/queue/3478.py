# Difficulty: Medium
# https://leetcode.com/problems/choose-k-elements-with-maximum-sum/
# Time - O(n log n), Space - O(n)

import heapq
from itertools import groupby
from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        nums1_argsorted = sorted(range(n), key=nums1.__getitem__)
        idx2sum = dict()
        min_heap = []
        current_sum = 0
        for _, group in groupby(nums1_argsorted, key=lambda i: nums1[i]):
            group = list(group)
            for idx in group:
                idx2sum[idx] = current_sum
            for idx in group:
                val = nums2[idx]
                if len(min_heap) < k:
                    heapq.heappush(min_heap, val)
                    current_sum += val
                elif val > min_heap[0]:
                    current_sum -= heapq.heapreplace(min_heap, val)
                    current_sum += val

        return [idx2sum[i] for i in range(n)]
