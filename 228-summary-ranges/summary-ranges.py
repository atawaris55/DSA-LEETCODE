class Solution(object):
    def summaryRanges(self, nums):
        i=0
        res=[]
        while i<len(nums):
            start=nums[i]
            while i+1<len(nums) and nums[i+1]==nums[i]+1:
                i+=1
            if start==nums[i]:
                res.append(str(nums[i]))
            else:
                res.append(str(start)+ '->' + str(nums[i]))
            i+=1
        print(res)
        return res

        
