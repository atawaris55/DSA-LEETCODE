class Solution(object):
    def longestOnes(self, nums, k):
        maxi=0
        n=len(nums)
        l=0
        r=0
        z=0
        for r in range(n):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            if z<=k:
                maxi=max(maxi,r-l+1)
        return maxi
