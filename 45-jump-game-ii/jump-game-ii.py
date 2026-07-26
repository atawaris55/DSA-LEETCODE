class Solution(object):
    def jump(self, nums):
        n=len(nums)
        l,r=0,0
        jump=0
        while r<n-1:
            far=0
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            jump+=1
        return jump