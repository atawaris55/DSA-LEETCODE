class Solution(object):
    def findDuplicate(self, nums):
        fq={}
        for num in nums:
            fq[num]=fq.get(num,0)+1
        for v in fq:
            if fq[v]>=2:
                return v