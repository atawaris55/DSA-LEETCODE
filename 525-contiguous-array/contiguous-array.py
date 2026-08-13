class Solution(object):
    def findMaxLength(self, nums):
        sum=0
        mp={0:-1}
        ans=0
        for i in range(len(nums)):
            if nums[i]==1:
                sum+=1
            else:
                sum-=1
            if sum in mp:
                ans=max(ans,i-mp[sum])
            else:
                mp[sum]=i
        return ans