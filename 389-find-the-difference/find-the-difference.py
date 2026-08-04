class Solution(object):
    def findTheDifference(self, s, t):
        frq={}
        for ch in s:
            if ch in frq:
                frq[ch]+=1
            else:
                frq[ch]=1
        for ch in t:
            if ch in frq:
                frq[ch]-=1
            else:
                frq[ch]=1
        for k,val in frq.items():
            if val!=0:
                return k
        
        