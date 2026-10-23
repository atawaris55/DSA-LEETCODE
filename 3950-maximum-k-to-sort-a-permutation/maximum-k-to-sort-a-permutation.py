class Solution(object):
    def sortPermutation(self, nums):
        r=-1
        for i,k in enumerate(nums):
            if i!=k:
                r&=k
        return max(r,0)