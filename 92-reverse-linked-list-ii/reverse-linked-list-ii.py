# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummyNode.next = head
        
        before = dummyNode
        pre = dummyNode
        
        for _ in range(1,left):
            before = before.next
            
        start = before.next
        current = start
        for _ in range(right-left+1):
            nextNode = current.next
            current.next = pre
            pre = current
            current = nextNode
        
        before.next = pre
        start.next = current
        
        return dummyNode.next
        