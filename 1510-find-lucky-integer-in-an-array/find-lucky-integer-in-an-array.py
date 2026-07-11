class Solution(object):
    def findLucky(self, arr):
        fre={}
        n=len(arr)
        for i in arr:

            fre[i]=fre.get(i,0)+1
        ans=-1
        for k,v in fre.items():
            if v==k:
                ans=max(ans,k)
                
        return ans