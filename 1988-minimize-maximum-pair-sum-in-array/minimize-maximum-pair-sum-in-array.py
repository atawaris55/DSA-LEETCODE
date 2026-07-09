class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        left=0
        right=len(nums)-1
        maxi=0
        while left<right:
            maxi=max(nums[left]+nums[right],maxi)
            left+=1
            right-=1
        return maxi

        