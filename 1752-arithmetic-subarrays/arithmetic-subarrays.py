class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        res=[]
        n=len(nums)
        for i in range(len(l)):
            g=nums[l[i]:r[i]+1]
            g.sort()
            diff = g[1] - g[0] 
            flag=True
            for j in range(1,len(g)-1):
                if g[j+1]-g[j]!=diff:
                    flag=False
                    break
            res.append(flag)
        return res


       