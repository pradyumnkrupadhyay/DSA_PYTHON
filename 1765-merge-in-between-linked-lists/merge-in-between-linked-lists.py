# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        prev_first, last = None, list1
        for i in range(b):
            if i == a-1:
                prev_first = last
            last = last.next
        prev_first.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = last.next
        last.next = None
        return list1
        