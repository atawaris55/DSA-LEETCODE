class Solution(object):
    def checkInclusion(self, s1, s2):
        count_s1={}
        count_s2={}
        left=0
        for i in range(len(s1)):
            count_s1[s1[i]]=count_s1.get(s1[i],0)+1
        for right in range(len(s2)):
            count_s2[s2[right]]=count_s2.get(s2[right],0)+1
            if right>=len(s1):
                count_s2[s2[left]]-=1
                if count_s2[s2[left]]==0:
                    del count_s2[s2[left]]
                left+=1
            if count_s1==count_s2:
                return True
        return False
                