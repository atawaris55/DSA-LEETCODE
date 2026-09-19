class Solution(object):
    def sumOfUnique(self, nums):
        fq={}
        total=0
        for i in range(len(nums)):
            fq[nums[i]]=fq.get(nums[i],0)+1
        for num in fq:
            if fq[num]==1:
                total+=num

        return total


        