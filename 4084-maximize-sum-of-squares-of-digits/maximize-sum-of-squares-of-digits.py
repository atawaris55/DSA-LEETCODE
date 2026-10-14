
class Solution(object):
    def maxSumOfSquares(self, num, sum):
        ans=""
        if sum>9*num:
            return ""
        while num:
            if sum>=9:
                ans+='9'
                sum-=9
            else:
                ans+=str(sum)
                sum=0
            num-=1
        return ans
