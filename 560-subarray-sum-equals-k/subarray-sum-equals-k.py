class Solution(object):
    def subarraySum(self, nums, k):
        mp={0:1}
        sum=0
        ans=0
        for num in nums:
            sum+=num
            if sum-k in mp:
                ans+=mp[sum-k]
            mp[sum]=mp.get(sum,0)+1
        return ans
        