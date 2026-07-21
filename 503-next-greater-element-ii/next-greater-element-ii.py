class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(2*n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i%n]:
                stack.pop()
            if i<n:
                if stack:
                    ans[i]=nums[stack[-1]]
            stack.append(i%n)
        return ans