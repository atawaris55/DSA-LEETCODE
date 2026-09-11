class Solution(object):
    def findRepeatedDnaSequences(self, s):
        left=0
        count={}
        ans=[]
        for right in range(len(s)):
            if right-left+1==10:
                count[s[left:right+1]]=count.get(s[left:right+1],0)+1
                left+=1
        for k,val in count.items():
            if val>=2:
                ans.append(k)
        return ans
