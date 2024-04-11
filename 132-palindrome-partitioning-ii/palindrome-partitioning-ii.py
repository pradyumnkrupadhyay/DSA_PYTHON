class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return 0

        is_visited = {0, }
        queue = deque([(0, 0)])

        while queue:
            cut, idx = queue.popleft()
            if s[idx:] == s[idx:][::-1]:
                return cut
            for i in range(idx + 1, length + 1):
                if i not in is_visited and s[idx:i] == s[idx:i][::-1]:
                    is_visited.add(i)
                    queue.append((cut + 1, i))