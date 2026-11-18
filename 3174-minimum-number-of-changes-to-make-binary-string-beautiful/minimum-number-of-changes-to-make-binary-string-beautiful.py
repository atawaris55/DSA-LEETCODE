class Solution(object):
    def minChanges(self, s):
        count=0
        for i in range(0,len(s),2):
            gp=s[i:i+2]
            if gp!='11' and gp!='00':
                count+=1
        return count
                
