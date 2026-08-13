class Solution(object):
    def subarraysDivByK(self, nums, k):
        mp={0:1}
        sum=0
        ans=0
        rem=0
        for num in nums:
            sum+=num
            rem=sum%k
            if rem in mp:
                ans+=mp[rem]
            mp[rem]=mp.get(rem,0)+1
        return ans
        