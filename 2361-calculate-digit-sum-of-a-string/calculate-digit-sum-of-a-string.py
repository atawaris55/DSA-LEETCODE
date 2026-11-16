class Solution(object):
    def digitSum(self, s, k):

        while len(s)>k:
            stin=''
            for i in range(0,len(s),k):
                gp=s[i:i+k]
                gp_sum=sum(int(digit) for digit in gp)
                stin+=str(gp_sum)
            s=stin
        return s

                


            
            