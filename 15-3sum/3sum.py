class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        res=set()
        for i in range(n):
            my_set=set()
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in my_set:
                    temp=tuple(sorted([nums[i],nums[j],third]))
                    res.add(temp)
                my_set.add(nums[j])
        return list(res)
        