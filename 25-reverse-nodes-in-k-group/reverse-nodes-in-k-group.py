# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k < 2:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        start = dummyNode
        end = head
        count = 0
        while end is not None:
            count += 1
            if count % k == 0:
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummyNode.next
    
    def reverse(self, start, end):
        prevNode= start
        currNode = start.next
        fNode = currNode
        while currNode != end:
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = temp
        start.next = prevNode
        fNode.next = currNode
        return fNode
       
        