# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next=head
        prev=dummy
        while prev.next is not None and prev.next.next is not None:
            first=prev.next
            sec=first.next

            first.next=sec.next
            sec.next=first
            prev.next=sec

            prev=first

        return dummy.next



