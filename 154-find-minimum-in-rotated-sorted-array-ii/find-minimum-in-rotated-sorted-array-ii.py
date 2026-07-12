class Solution(object):
    def findMin(self, nums):
        minimum=nums[0]
        for i in range(len(nums)):
            if nums[i]<minimum:
                minimum=nums[i]
        return minimum