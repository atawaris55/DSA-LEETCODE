class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        closet=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if abs(total_sum-target)<abs(closet-target):
                    closet=total_sum
                if total_sum<target:
                    j+=1
                elif total_sum>target:
                    k-=1
                else:
                    return total_sum
        return closet