class Solution(object):
    def majorityElement(self, nums):
        seen={}
        n=len(nums)//3
        res=[]
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for k,val in seen.items():
            if val>n:
                res.append(k)
        return res
                