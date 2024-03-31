# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
                
        while True:
            
            if len(queue) == 0:
                break
                
            right, left = 0, len(queue) - 1
            while right < left:
                if queue[right] is None and queue[left] is None:
                    right += 1
                    left -= 1
                    continue
                    
                if queue[right] is not None and queue[left] is not None and (queue[right].val == queue[left].val):
                    right += 1
                    left -= 1
                    continue
                    
                return False
            
            cache = []
            for node in queue:
                if node is None:
                    continue
                
                cache.append(node.left)
                cache.append(node.right)
                
            queue = cache
            
        return True