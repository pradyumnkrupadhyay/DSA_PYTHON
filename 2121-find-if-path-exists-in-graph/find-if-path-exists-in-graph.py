class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        def dfs(node, visited):
            if node == destination:
                return True

            visited[node] = 1
            for nei in neis[node]:
                if visited[nei] == 0 and dfs(nei, visited):
                    return True
            return False

        neis = collections.defaultdict(list)
        for s, e in edges:
            neis[s].append(e)
            neis[e].append(s)
        visited = [0] * n
        return dfs(source, visited)