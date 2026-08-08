class Solution(object):
    def smallestNumber(self, n, t):
        for i in range(n,n+10):
            x=i
            pro=1
            while i>0:
                pro*=i%10
                i//=10
            if pro%t==0:
                return x
            i+=1

