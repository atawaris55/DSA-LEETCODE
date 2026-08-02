class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ameer=max(candies)
        res=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= ameer:
                res.append(True)
            else:
                res.append(False)
        return res