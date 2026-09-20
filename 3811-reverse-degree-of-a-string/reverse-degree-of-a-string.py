class Solution(object):
    def reverseDegree(self, s):
        summ=0
        for i in range(len(s)):
            val=ord('z')-ord(s[i])+1
            summ+=val*(i+1)
        return summ
        