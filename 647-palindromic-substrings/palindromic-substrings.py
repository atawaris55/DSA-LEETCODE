class Solution(object):
    def countSubstrings(self,s):
        count=0
        for i in range(len(s)):
            left=i #odd k liye ha beech s nikaal rhe h
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            left=i
            right=i+1 #even k liye h beech s nikal rhe h
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        return count