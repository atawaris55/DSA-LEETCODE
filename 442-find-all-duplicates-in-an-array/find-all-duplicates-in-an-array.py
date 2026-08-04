class Solution(object):
    def findDuplicates(self, nums):
        res=[]
        arr=[0]*(len(nums)+1)
        for i in nums:
            if arr[i]==0:
               
                arr[i]=1
            else:
                res.append(i)
        return res
