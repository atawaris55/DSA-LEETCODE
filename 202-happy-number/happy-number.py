class Solution(object):
    def isHappy(self, n):
        dig=n
        if n==1 or n==7:
            return True
        elif n<10:
            return False
        s=0
        while dig>0:
            
            digi=dig%10
            s=s+digi**2

            dig=dig//10
        return self.isHappy(s)
