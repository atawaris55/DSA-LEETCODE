class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc=1
        dec=1
        ans=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1
                dec=1
                
            elif nums[i-1]>nums[i]:
                dec+=1
                inc=1
            else:
                inc=1
                dec=1
            ans=max(inc,dec,ans)
        return ans