class Solution(object):
    def findDuplicate(self, nums):
        seen=[0]*len(nums)
        for e in nums:
            if seen[e]:
                return e
            seen[e]=1