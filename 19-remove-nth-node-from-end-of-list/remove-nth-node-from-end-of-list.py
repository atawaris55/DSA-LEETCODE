# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length=0
        temp=head
        while temp is not None:
            length+=1
            temp=temp.next
        if length==n:
            new_head=head.next
            del head
            return new_head
        pos=length-n
        temp=head
        count=1
        while count<pos:
            temp=temp.next
            count+=1
        temp.next=temp.next.next
        return head