class Solution(object):
    def sumOfUnique(self, nums):
        fq={}
        total=0
        for num in nums:
            fq[num]=fq.get(num,0)+1
        for num in fq:
            if fq[num]==1:
                total+=num

        return total


        