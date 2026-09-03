# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        if head is None:
            return head
        dummy1 = ListNode(0)   
        dummy2 = ListNode(0)
        small=dummy1
        large=dummy2
        node=head
        while node:
            next_node=node.next
            if node.val<x:
                small.next=node
                small=small.next
            else:
                large.next=node
                large=large.next
            node=next_node
        small.next=dummy2.next
        large.next=None
        return dummy1.next