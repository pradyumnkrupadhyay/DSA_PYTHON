class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        citations.sort(reverse=True)
        p = 0
        while p < len(citations):
            if citations[p] >= p + 1:
                p += 1
            else:
                break
        return p
        