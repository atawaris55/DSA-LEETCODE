class Solution(object):
    def subarraysDivByK(self, nums, k):
        mp={0:1}
        sum=0
        ans=0
        rem=0
        for num in nums:
            sum+=num
            
            if sum%k in mp:
                ans+=mp[sum%k]
            mp[sum%k]=mp.get(sum%k,0)+1
        return ans
        