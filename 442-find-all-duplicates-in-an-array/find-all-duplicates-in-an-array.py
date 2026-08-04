class Solution(object):
    def findDuplicates(self, nums):
        frq={}
        res=[]
        for num in nums:
            if num in frq:
                frq[num]+=1
            else:
                frq[num]=1
        for k,v in frq.items():
            if v>1:
                res.append(k)
        return res
        