class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        hold = [float('-inf')] * (n + 1)
        sold = [0] * (n + 1)
        rest = [0] * (n + 1)

        for i in range(1, n + 1):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i - 1])  # Buy or keep holding
            sold[i] = max(sold[i - 1], hold[i - 1] + prices[i - 1])  # Sell or keep sold
            rest[i] = max(rest[i - 1], sold[i - 1])  # Cooldown or keep resting

        return sold[n]
        