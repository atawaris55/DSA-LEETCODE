class Solution(object):
    def maxAlternatingSum(self, nums):
        k=len(nums)//2
        a=[]
        total=0
        for num in nums:
            a.append(num*num)
        a.sort()
        total+=sum(a[k:])
        total-=sum(a[:k])
        return total

        
        