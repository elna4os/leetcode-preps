# Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
# Time - O(m + n), Space - O(k) where k is the max ID

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        # Assumption: IDs are in the range 1 to 1000
        n_ids_max = 1000
        # Array to hold summed values for each ID
        id_arr = [0] * n_ids_max
        max_id = -1
        # Merge the two arrays
        while i < m or j < n:
            # Process nums1
            if i < m:
                id_, val = nums1[i]
                if id_ > max_id:
                    max_id = id_
                id_arr[id_ - 1] += val
                i += 1
            # Process nums2
            if j < n:
                id_, val = nums2[j]
                if id_ > max_id:
                    max_id = id_
                id_arr[id_ - 1] += val
                j += 1
        res = []
        # Construct the result array
        for i in range(max_id):
            if id_arr[i]:
                res.append((i + 1, id_arr[i]))

        return res
