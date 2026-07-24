class Solution(object):
    def findContentChildren(self, g, s):
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        left,right,count=0,0,0
        while left<n and right<m:
            if g[left]<=s[right]:
                count+=1
                left+=1
            right+=1
        return count