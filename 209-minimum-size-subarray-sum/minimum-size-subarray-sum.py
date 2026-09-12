class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        n=0
        ans=float("inf")
        for right in range(len(nums)):
            n+=nums[right]
            while n>=target:
                ans=min(ans,right-left+1)
                n-=nums[left]
                left+=1
        if ans==float("inf"):
            return 0
        return ans
