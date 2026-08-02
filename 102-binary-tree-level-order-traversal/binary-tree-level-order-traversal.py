# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        res=[]
        queqe=deque()
        queqe.append(root)
        while queqe:
            level=[]
            
            for _ in range(len(queqe)):
                e=queqe.popleft()
                level.append(e.val)
                if e.left is not None:
                    queqe.append(e.left)
                if e.right is not None:
                    queqe.append(e.right)
            res.append(level)
        return res
