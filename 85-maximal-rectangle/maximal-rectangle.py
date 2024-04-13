class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        heights = [0 for _ in range(len(matrix[0]) + 1)]
        ans = 0
        for row in matrix:
            for i in range(len(matrix[0])):
                if row[i] == "1":
                    heights[i] = heights[i] + 1
                else:
                    heights[i] = 0
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans