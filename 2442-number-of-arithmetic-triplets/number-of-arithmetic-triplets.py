class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        ans=0
        for num in nums:
            if num +diff in nums and num + 2*diff in nums:
                ans+=1
        return ans 

        