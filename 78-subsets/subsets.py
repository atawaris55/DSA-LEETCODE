class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        tall_sub=1<<n
        res=[]
        for num in range(tall_sub):
            lst=[]
            for i in range(n):
                if num&(1<<i)!=0:
                    lst.append(nums[i])
            res.append(lst)
        return res