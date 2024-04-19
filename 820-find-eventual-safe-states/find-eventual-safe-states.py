class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        visited = [0 for i in range(len(graph))]
        result = []

        def is_safe(curNode):
            if visited[curNode] != 0:
                return visited[curNode] == 2
            visited[curNode] = 1
            for newNode in graph[curNode]:
                if not is_safe(newNode):
                    return False
            visited[curNode] = 2
            return True

        for i in range(len(graph)):
            if is_safe(i):
                result.append(i)

        return result

        