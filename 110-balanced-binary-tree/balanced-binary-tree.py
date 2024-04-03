# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
         return self.getBalanceHeight(root) != -1

 
    def getBalanceHeight(self, root):
        if root is None:
            return 0;

        leftHeight = self.getBalanceHeight(root.left)
        # if left child tree is not balanced, return -1 directly to stop recursion
        if leftHeight < 0:
            return -1

        rightHeight = self.getBalanceHeight(root.right)
        # if right child tree is not balanced, return -1 directly to stop recursion
        if rightHeight < 0:
            return -1

        if math.fabs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1
            