class Solution(object):
    def checkRecord(self, s):
        left=0
        count_l=0
        count_a=0
        for right in range(len(s)):
            if s[right]=='L':
                count_l+=1
            else:
                count_l=0
            if count_l==3:
                return False
            if s[right]=='A':
                count_a+=1
            if count_a==2:
                return False
        return True

        
