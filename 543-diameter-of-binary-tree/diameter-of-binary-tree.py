# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        dia=[0]
        def solve(node):
            if node ==None:
                return 0
            lefth=solve(node.left)
            righth=solve(node.right)
            dia[0]=max(dia[0],lefth+righth)
            return 1+max(lefth,righth)
        solve(root)
        return dia[0]
