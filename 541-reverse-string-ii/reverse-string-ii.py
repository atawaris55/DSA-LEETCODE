class Solution(object):
    def reverseStr(self, s, k):
        s=list(s)
        for i in range(0,len(s)-1,2*k):
            firest_occur=s[i:i+k]
            rev_occ=firest_occur[::-1]
            s[i:i+k]=rev_occ
        return "".join(s)