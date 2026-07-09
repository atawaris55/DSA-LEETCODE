class Solution(object):
    def rangeSum(self, nums, n, left, right):
        res=[]
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                res.append(s)
        res.sort()
        mod=10**9+7
        return (sum(res[left-1:right]))%mod
