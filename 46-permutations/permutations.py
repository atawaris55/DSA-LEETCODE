class Solution(object):
    def permute(self, nums):
        n=len(nums)
        used=[False]*n
        res=[]
        def backtrack(comb):
            if len(comb)==len(nums):
                res.append(comb[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                comb.append(nums[i])
                used[i]=True
                backtrack(comb)
                used[i]=False
                comb.pop()
        backtrack([])
        return res

        