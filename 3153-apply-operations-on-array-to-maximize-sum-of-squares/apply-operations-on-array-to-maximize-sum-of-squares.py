class Solution(object):
    def maxSum(self, nums, k):
        count=[0]*31
        for num in nums:
            for i in range(31):
                if num & (1<<i):
                    count[i]+=1
        ans=0
        for _ in range(k):
            num=0
            for i in range(31):
                if count[i]>0:
                    num |= (1<<i)
                    count[i]-=1
            ans+=num*num
        return ans%(10**9+7)