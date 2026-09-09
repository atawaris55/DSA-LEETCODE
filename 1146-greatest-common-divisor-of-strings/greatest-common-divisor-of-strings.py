
class Solution(object):
    
    def gcdOfStrings(self, str1, str2):
        
        res=''
        if str1+str2!=str2+str1:
            return ""
        a=len(str1)
        b=len(str2)
        while b:
            a,b=b,a%b
        
        res+=str1[:a]
        return res