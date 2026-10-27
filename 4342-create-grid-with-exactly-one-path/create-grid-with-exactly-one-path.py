class Solution(object):
    def createGrid(self, m, n):
        ans=[]
        for i in range(m):
            if i==0:
                ans.append('.'*n)
            else:
                ans.append('#'*(n-1)+'.')
        return ans
