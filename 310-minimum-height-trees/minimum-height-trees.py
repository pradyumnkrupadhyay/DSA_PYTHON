class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n==1: return [0]
        degrees = [0] * n
        adj = [[] for _ in range(n)]
        for l,r in edges:
            adj[l].append(r)
            adj[r].append(l)
            degrees[l] += 1
            degrees[r] += 1
        
        from queue import Queue
        q = Queue()
        for i,degree in enumerate(degrees):
            if degree==1:
                q.put(i)
        
        ans = []
        while not q.empty():
            ans = []
            for _ in range(q.qsize()):
                cur = q.get()
                ans.append(cur)
                for i in adj[cur]:
                    degrees[i] -= 1
                    if degrees[i]==1:
                        q.put(i)
        return ans

        