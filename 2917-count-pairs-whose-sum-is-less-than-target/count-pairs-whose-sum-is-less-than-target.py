class Solution(object):
    def countPairs(self, nums, target):
   
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] < target:
                    res.append((i,j))
        return len(res)
