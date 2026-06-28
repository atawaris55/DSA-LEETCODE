class Solution(object):
    def pivotIndex(self, nums):
        n=len(nums)
        total=sum(nums)
        left=0
        for i in range(n):
            right=total-left-nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1

        

            