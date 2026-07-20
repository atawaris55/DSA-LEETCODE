class Solution(object):
    def twoSum( self,nums, target):
        seen={}
        n=len(nums)
        for i in range(n):
            compliment=target-nums[i]
            if compliment in seen:
                return [seen[compliment],i]
            seen[nums[i]]=i








        