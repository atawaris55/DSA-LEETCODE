class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        ans=float('inf')
        total=0
        n=len(nums)
        for k in range(l,r+1):
            total=sum(nums[:k])
            if total>0:
                ans=min(ans,total)
            for i in range(k,n):
                total+=nums[i]-nums[i-k]
                if total>0:
                    ans=min(ans,total)
        return -1 if ans==float('inf') else ans
