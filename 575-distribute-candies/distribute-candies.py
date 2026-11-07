class Solution(object):
    def distributeCandies(self, candyType):
        dic={}
        n=len(candyType)
        for i in range(len(candyType)):
            dic[candyType[i]]=dic.get(candyType[i],0)+1
        
        if n/2 < len(dic):
            return n/2
        else:
            return len(dic)
