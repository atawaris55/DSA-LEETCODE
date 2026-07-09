class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        n=len(nums)
        l=0
        r=n-1
        count=0
        while l<r:
            sum=nums[l]+nums[r]
            if sum<target:
                count+= r-l
                l+=1
            else:
                
                r-=1
        return count
            
