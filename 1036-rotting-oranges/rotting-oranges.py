class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        unaffected_houses = 0

        # Initialize queue with infected houses and count unaffected houses
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, day)
                elif grid[i][j] == 1:
                    unaffected_houses += 1

        if unaffected_houses == 0:
            return 0  # All houses are already infected

        days = 0
        while queue:
            row, col, days = queue.popleft()

        # Check adjacent cells
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2  # Infect the house
                    queue.append((new_row, new_col, days + 1))
                    unaffected_houses -= 1
                    if unaffected_houses == 0:
                        return days + 1  # All houses are infected

        return -1  # At least one house remains unaffected

        