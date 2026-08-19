# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        fast=head
        for i in range(k-1):
            fast=fast.next
        first=fast
        slow=head
        while fast.next:
            slow=slow.next
            fast=fast.next
        second=slow
        first.val,second.val=second.val,first.val
        return head
