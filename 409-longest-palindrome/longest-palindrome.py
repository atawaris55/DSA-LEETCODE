class Solution(object):
    def longestPalindrome(self, s):
        fq={}
        
        for i in range(len(s)):
            fq[s[i]]=fq.get(s[i],0)+1
        n=len(s)
        odd=0
        for ch in fq:
            if fq[ch]%2!=0:
                n-=1
                odd+=1
        if odd>0:
            n+=1   
        
        return n
