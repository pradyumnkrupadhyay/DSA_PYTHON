# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        list1 = []
        list2 = []

        def inorder(node, lst):
            if not node:
                return
            inorder(node.left, lst)
            lst.append(node.val)
            inorder(node.right, lst)

        inorder(root1, list1)
        inorder(root2, list2)

        def merge(x, y):
            ans = []
            i = 0
            j = 0
            while i < len(x) and j < len(y):
                if x[i] <= y[j]:
                    ans.append(x[i])
                    i += 1
                else:
                    ans.append(y[j])
                    j += 1
            ans += x[i:]
            ans += y[j:]
            return ans

        return merge(list1, list2)
        