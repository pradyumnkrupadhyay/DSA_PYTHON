class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            smallest_two = heapq.nsmallest(2, grid[i-1])
            for j in range(len(grid[0])):
                grid[i][j] += smallest_two[1] if grid[i-1][j] == smallest_two[0] else smallest_two[0]
        return min(grid[-1])
        