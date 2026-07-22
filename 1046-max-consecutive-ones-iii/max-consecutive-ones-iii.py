class Solution(object):
    def longestOnes(self, nums, k):

        n=len(nums)
        maxi,r,z,l=0,0,0,0

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
