# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        self.ans = "{"
        
        def dfs(node, cur_ans):
            cur_ans += chr(ord('a') + node.val)
            if node.left is None and node.right is None:
                cur_ans = cur_ans[::-1]
                self.ans = min(self.ans, cur_ans)
                return
            if node.left is not None:
                dfs(node.left, cur_ans)
            if node.right is not None:
                dfs(node.right, cur_ans)
        
        dfs(root, "")
        return self.ans