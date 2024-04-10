class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        cnt = 0
        for i, val in enumerate(tickets):
            cnt += min(tickets[k] - bool(k < i), val)
        return cnt