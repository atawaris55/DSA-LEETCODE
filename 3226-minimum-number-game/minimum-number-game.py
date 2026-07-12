class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        n=len(nums)
        for i in range(0,n-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
            
        return nums
