class Solution(object):
    def canAliceWin(self, n):
        if n<10:
            return False
        remove=10
        count=0
        while n>=remove:
            n-=remove
            remove-=1
            count+=1
        return count%2==1




