class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        n=len(nums)
        ls=[]
        for i in range(n):
            for k in range(i+1,n):
                if nums[k]-nums[i]==2*diff:
                    mid=nums[i]+diff
                    if mid in nums:
                        ls.append((nums[i],mid,nums[k]))
        print(ls)
        return len(ls)

        