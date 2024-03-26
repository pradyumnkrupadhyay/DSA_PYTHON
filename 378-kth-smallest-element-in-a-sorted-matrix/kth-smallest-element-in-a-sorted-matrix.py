class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for x in matrix:
            for y in x:
                heapq.heappush(minHeap, y)
        index = 0
        while index<k-1:
            heapq.heappop(minHeap)
            index+=1
        return minHeap[0]
        