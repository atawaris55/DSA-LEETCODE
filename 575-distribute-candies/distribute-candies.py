class Solution(object):
    def distributeCandies(self, candyType):
        dic={}
        n=len(candyType)
        for i in range(len(candyType)):
            dic[candyType[i]]=dic.get(candyType[i],0)+1
        
        return min(n/2,len(dic))
