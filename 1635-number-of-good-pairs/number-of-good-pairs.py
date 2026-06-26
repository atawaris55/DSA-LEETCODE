class Solution(object):
    def numIdenticalPairs(self, nums):
        # res=[]
        count=0
        n=len(nums)
        for i in range(n):
            # count=[]
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    count+=1
        return count
        