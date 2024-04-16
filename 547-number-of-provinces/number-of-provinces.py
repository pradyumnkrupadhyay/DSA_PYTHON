class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        res = 0
        visit = set()
        for i in range(n):
            if i in visit:
                continue
            s = [i]
            visit.add(i)
            res += 1
            while s:
                cur = s.pop()
                for j in range(n):
                    if j not in visit and isConnected[cur][j] == 1:
                        s.append(j)
                        visit.add(j)
        return res