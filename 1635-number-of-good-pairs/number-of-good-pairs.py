class Solution(object):
    def numIdenticalPairs(self, nums):
        freq={}
        n=len(nums)
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        ans=0
        for val in freq.values():
            if val>=2:
                ans+=val*(val-1)/2
        return ans


