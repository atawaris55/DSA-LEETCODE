class Solution(object):
    def frequencySort(self, s):
        fq={}
        op=""
        for i in range(len(s)):
            fq[s[i]]=fq.get(s[i],0)+1
        sorted_fq=sorted(fq,key= lambda ch:fq[ch],reverse=True)

        for ch in sorted_fq:
            op+=ch*fq[ch]
        return op