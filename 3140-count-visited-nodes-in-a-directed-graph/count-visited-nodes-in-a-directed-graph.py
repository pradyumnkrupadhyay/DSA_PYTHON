class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:

        def find_cycles(adj):
            result = [0]*len(adj)
            lookup = [0]*len(adj)
            stk = []  # added
            idx = 0
            for u in range(len(adj)):
                prev = idx
                while not lookup[u]:
                    idx += 1
                    lookup[u] = idx
                    stk.append(u)  # added
                    u = adj[u]
                if lookup[u] > prev:
                    l = idx-lookup[u]+1
                    for _ in range(l):  # added
                        result[stk.pop()] = l
                while stk:  # added
                    result[stk[-1]] = result[adj[stk[-1]]]+1
                    stk.pop()
            return result
        
        return find_cycles(edges)
        