class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        # res=[True]*len(l)
        # n=len(nums)
        # for i in range(len(l)):
        #     g=nums[l[i]:r[i]+1]
        #     g.sort()
        #     diff = g[1] - g[0] 
        #     flag=True
        #     for j in range(1,len(g)-1):
        #         if g[j+1]-g[j]!=diff:
        #             res[i]=False
        #             break
        # return res
        res=[True]*len(l)
        for i in range(len(l)):
            lt=nums[l[i]:r[i]+1]
            lt.sort()
            diff=lt[1]-lt[0]
            
            for j in range(1,len(lt)-1):
                if diff!=lt[j+1]-lt[j]:
                    res[i]=False
                    break
        return res            
                  

       