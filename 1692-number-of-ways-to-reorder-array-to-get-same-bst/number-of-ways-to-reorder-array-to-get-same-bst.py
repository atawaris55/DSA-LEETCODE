class Solution(object):
    def numOfWays(self, nums):
        mod=10**9+7
        def comb(n,r):
            ans=1
            for i in range(r):
                ans=ans*(n-i)//(i+1)
            return ans
        def dfs(nums):
            if len(nums)<3:
                return 1
            left_node=[a for a in nums if a <nums[0]]
            right_node=[a for a in nums if a >nums[0]]
            return dfs(left_node)*dfs(right_node)*comb(len(nums)-1,len(left_node))%mod
        return (dfs(nums)-1)%mod
        