class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        

        def iter_dfs(u, target):
            stk = [(1, (u, -1))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p = args
                    lookup[u] += 1
                    if u == target:
                        return
                    stk.append((2, (u,)))
                    for v in reversed(adj[u]):
                        if v == p:
                            continue
                        stk.append((1, (v, u)))
                elif step == 2:
                    u = args[0]
                    lookup[u] -= 1
    
            lookup[u] += 1
            if u == target:
                return True
            for v in adj[u]:
                if v == p:
                    continue
                if dfs(v, u, target):
                    return True
            lookup[u] -= 1
            return False
    
        def iter_dfs2():
            result = [price[0]*lookup[0], (price[0]//2)*lookup[0]]
            stk = [(1, (0, -1, result))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, ret = args
                    for v in reversed(adj[u]):
                        if v == p:
                            continue
                        new_ret = [price[v]*lookup[v], (price[v]//2)*lookup[v]]
                        stk.append((2, (new_ret, ret)))
                        stk.append((1, (v, u, new_ret)))
                elif step == 2:
                    new_ret, ret = args
                    ret[0] += min(new_ret)
                    ret[1] += new_ret[0]
            return min(result)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = [0]*n
        for u, v in trips:
            iter_dfs(u, v)
        return iter_dfs2()
    