class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1  # Base case: one way to make sum 0 (empty combination)

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]
        