class Solution(object):
    def customSortString(self, order, s):
        fq={}
        op=""
        n=len(s)
        for i in range(n):
            fq[s[i]]=fq.get(s[i],0)+1
        for ch in order:
            if ch in fq:
                op+=ch*fq[ch]
        for ch in fq:
            if ch not in op:
                op+=ch*fq[ch]
                
        return op
        