class Solution(object):
    def subarraySum(self, nums, k):
        mp={0:1}
        summ=0
        ans=0
        for num in nums:
            summ+=num
            if summ-k in mp:
                ans+=mp[summ-k]
            mp[summ]=mp.get(summ,0)+1
        return ans
        