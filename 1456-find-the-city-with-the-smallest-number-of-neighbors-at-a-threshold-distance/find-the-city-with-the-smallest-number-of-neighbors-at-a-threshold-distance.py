class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for x, y, d in edges:
            dist[x][y] = dist[y][x] = d
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        ans = -1
        cnt = float("inf")
        for i in range(n):
            cur_cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cur_cnt += 1
            if cur_cnt <= cnt:
                cnt = cur_cnt
                ans = i
        return ans
        