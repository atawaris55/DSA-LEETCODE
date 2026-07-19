class Solution(object):
    def findMissingElements(self, nums):
        a=[]
        data=set(nums)
        for i in range(min(nums),max(nums)):
            if i not in data:
                a.append(i)
        return a

