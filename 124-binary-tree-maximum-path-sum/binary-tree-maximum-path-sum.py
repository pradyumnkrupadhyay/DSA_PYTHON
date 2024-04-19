# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)
            
            if maxLeft < 0:
                maxLeft = root.val
            else:
                maxLeft += root.val
            
            if maxRight < 0:
                maxRight = root.val
            else:
                maxRight += root.val

            self.maximum = max(self.maximum, maxLeft + maxRight - root.val)
            return max(maxLeft, maxRight)
           
        self.maximum = -float('inf')
        dfs(root)
        return self.maximum
