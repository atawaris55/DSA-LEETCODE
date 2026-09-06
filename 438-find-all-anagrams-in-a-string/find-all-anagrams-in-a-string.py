class Solution(object):
    def findAnagrams(self, s, p):
        count_p={}
        count_win={}
        ans=[]
        left=0
        for i in range(len(p)):
            count_p[p[i]]=count_p.get(p[i],0)+1
        for right in range(len(s)):
            count_win[s[right]]=count_win.get(s[right],0)+1
            if right>=len(p):
                count_win[s[left]]-=1
                if count_win[s[left]]==0:
                    del count_win[s[left]]                        
                left+=1
            if count_win==count_p:
                ans.append(left)
        return ans
                
                
