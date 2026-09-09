class Solution(object):
    def countCommas(self, n):
        x=1000
        ans=0
        while x<=n:
            ans+=n-x+1
            x*=1000
        return ans        