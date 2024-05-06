class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        if n == 1:
            return 1

        ans = [0 for _ in range(n)]

        def solve(i):
            if ans[i] == 0:
                if i == 0:
                    if ratings[i] > ratings[i + 1]:
                        ans[i] = solve(i + 1) + 1
                    else:
                        ans[i] = 1
                elif i == n - 1:
                    if ratings[i] > ratings[i - 1]:
                        ans[i] = solve(i - 1) + 1
                    else:
                        ans[i] = 1
                else:
                    if ratings[i] <= ratings[i - 1] and ratings[i] <= ratings[i + 1]:
                        ans[i] = 1
                    elif ratings[i] > ratings[i - 1] and ratings[i] <= ratings[i + 1]:
                        ans[i] = solve(i - 1) + 1
                    elif ratings[i] <= ratings[i - 1] and ratings[i] > ratings[i + 1]:
                        ans[i] = solve(i + 1) + 1
                    else:
                        ans[i] = max(solve(i - 1), solve(i + 1)) + 1
            return ans[i]

        for i in range(n):
            _ = solve(i)
        return sum(ans)