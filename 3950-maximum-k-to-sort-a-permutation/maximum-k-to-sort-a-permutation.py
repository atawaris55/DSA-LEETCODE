class Solution(object):
    def sortPermutation(self, nums):
        i=0
        k=-1
        while i<len(nums):
            current_idx=nums[i]
            if 0<=current_idx<len(nums) and nums[i]!=nums[current_idx]:
                if k==-1:
                    k= nums[i] & nums[current_idx]
                else:
                    k = k &  nums[i] & nums[current_idx]
                i+=1

            else:
                i+=1
        if k==-1:
            return 0
   
        return k
        
