class Solution(object):
    def findPeakElement(self, nums):
        num=max(nums)
        return nums.index(num)