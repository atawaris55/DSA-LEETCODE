class Solution(object):
    def getLucky(self, s, k):
        num=''
        for ch in s:
            num+=str(ord(ch)-ord('a')+1)
        print(num)
        while k>0:
        
            jod=0
            for dig in num:
                jod+=int(dig)
            num=str(jod)
            k-=1
        return jod
                

