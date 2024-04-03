# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        vals = []
        while head:
            vals += head.val,
            head = head.next

        return self.recursive(vals, 0, len(vals) - 1)

    def recursive(self, vals, first, last):
        if first > last:
            return None
        if first == last:
            return TreeNode(vals[first])

        middle = first + (last - first) // 2
        root = TreeNode(vals[middle])

        root.left = self.recursive(vals, first, middle - 1)
        root.right = self.recursive(vals, middle + 1, last)

        return root