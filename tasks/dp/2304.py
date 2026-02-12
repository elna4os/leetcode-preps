# Difficulty: Medium
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/
# Time - O(m * n^2), Space - O(n)

from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        costs = grid[0]  # Define min cost to reach each cell in a row
        for i in range(1, m):  # For each subsequent row
            new_costs = []  # Min costs to reach each cell in the current row
            for j in range(n):  # For each cell in the current row
                target = grid[i][j]  # Value of the current cell
                min_val = None  # Min cost to reach the current cell
                for k in range(n):  # For each cell in the previous row
                    prev_cell = grid[i - 1][k]  # Value of the previous cell
                    edge_cost = moveCost[prev_cell][j]  # Cost to move from previous cell to current cell
                    prev_cost = costs[k]  # Min cost to reach the previous cell
                    c = prev_cost + edge_cost + target  # Total cost to reach the current cell
                    if min_val is None or c < min_val:
                        min_val = c
                new_costs.append(min_val)
            # Update costs for the next iteration
            costs = new_costs

        return min(costs)
