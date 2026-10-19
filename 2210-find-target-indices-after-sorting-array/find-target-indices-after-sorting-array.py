class Solution(object):
    def targetIndices(self, nums, target):
        n=len(nums)
        
        # for i in range(n-1):
        #     for j in range(n-1-i):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        nums.sort()
        ans=[]
        for i in range(n):
            if nums[i]==target:
                ans.append(i)
        return ans
