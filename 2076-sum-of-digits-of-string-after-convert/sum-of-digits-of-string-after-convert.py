class Solution(object):
    def getLucky(self, s, k):
        num=''
        for ch in s:
            num+=str(ord(ch)-ord('a')+1)
        while k>0:
            num_int=int(num)
            jod=0
            while num_int >0:
                dig=num_int%10
                jod+=dig
                num_int=num_int//10
            num=str(jod)
            k-=1
        return jod
                

