class Solution(object):
    def singleNumber(self, nums):
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        for k , val in count.items():
            if val ==1 :
                return k