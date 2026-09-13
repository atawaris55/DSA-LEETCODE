class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        n=len(nums)
        count=0
        left=0
        pro=1
        if k<2:
            return 0
        for right in range(n):
            pro*=nums[right]
            while pro>=k:
                pro=pro/nums[left]
                left+=1
            count+=right-left+1

        return count

