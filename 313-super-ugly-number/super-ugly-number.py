class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:


        dp = [0] * n
        dp[0] = 1
        pointer = [0] * len(primes)

        for i in range(1, n):
            next_ugly = float('inf')
            for j in range(len(primes)):
                next_ugly = min(next_ugly, primes[j] * dp[pointer[j]])
            dp[i] = next_ugly

        # Update pointers
            for j in range(len(primes)):
                if next_ugly == primes[j] * dp[pointer[j]]:
                    pointer[j] += 1

        return dp[n - 1]
        