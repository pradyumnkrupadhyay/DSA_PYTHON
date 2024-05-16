class Solution:
    def numSquares(self, n: int) -> int:

        
        if n <= 3:
            return n
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            for x in range(1, int(i**0.5) + 1):
                temp = x * x
                if temp > i:
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i - temp])
        return dp[n]

#print(getMinSquares(6))  # Output: 3
