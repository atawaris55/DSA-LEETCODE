# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return head
        if head.next is None:
            return head
        length=0
        node=head

        while node:
            length+=1
            node=node.next
        node=head
        k=k%length
        if k==0:
            return head
        while node.next:
            node=node.next
        
        node.next=head

        tail1=length-k
        for i in range(tail1):
            node=node.next

        new_head=node.next
        node.next=None
        return new_head

            
