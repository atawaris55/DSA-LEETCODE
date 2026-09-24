class Solution(object):
    def smallestIndex(self, nums):
        
        for i in range(len(nums)):
            count=0
            while nums[i]>0:
                count+=nums[i]%10
                nums[i]/=10
            if count==i:
                return i
                
        return -1

