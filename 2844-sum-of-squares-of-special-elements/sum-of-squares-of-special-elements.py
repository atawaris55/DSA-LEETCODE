class Solution(object):
    def sumOfSquares(self, nums):
        ans=0
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                ans+=nums[i]*nums[i]
        return ans
