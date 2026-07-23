class Solution(object):
    def totalFruit(self, fruits):
        n=len(fruits)
        l=0
        pick={}
        max_len=0


        for i in range(n):
            pick[fruits[i]]=pick.get(fruits[i],0)+1
            if len(pick)>2:
                pick[fruits[l]]-=1
                if pick[fruits[l]]==0:
                    del pick[fruits[l]]
                l+=1
            max_len=max(max_len,i-l+1)
        return max_len

            
            

