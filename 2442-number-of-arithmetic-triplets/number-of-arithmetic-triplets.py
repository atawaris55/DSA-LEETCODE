class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        ans=0
        seen=set(nums)
        for num in nums:
            if num +diff in seen and num + 2*diff in seen:
                ans+=1
        return ans 

        