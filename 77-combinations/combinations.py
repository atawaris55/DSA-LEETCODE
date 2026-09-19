class Solution(object):
    def combine(self, n, k):
        res=[]
        def backtract(start,comb):
            if len(comb)==k:
                res.append(comb[:])
                return 
            for i in range(start,n+1):
                comb.append(i)
                backtract(i+1,comb)

                comb.pop()
        backtract(1,[])
        return res
        