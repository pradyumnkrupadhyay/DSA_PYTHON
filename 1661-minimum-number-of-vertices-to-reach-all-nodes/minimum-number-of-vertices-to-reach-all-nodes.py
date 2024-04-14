class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        
        result = []
        lookup = set()
        for u, v in edges:
            lookup.add(v)
        for i in range(n):
            if i not in lookup:
                result.append(i)
        return result