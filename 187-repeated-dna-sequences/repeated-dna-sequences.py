class Solution(object):
    def findRepeatedDnaSequences(self, s):
        left=0
        count={}
        ans=[]
        for right in range(len(s)):
            if right-left+1==10:
                seq=s[left:right+1]
                count[seq]=count.get(seq,0)+1

                if count[seq]==2:
                    ans.append(seq)
                left+=1


        return ans
