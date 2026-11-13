class Solution(object):
    def finalValueAfterOperations(self, operations):
        ans=0
        for i in range(len(operations)):
            if operations[i]=="--X" :
                ans-=1
            elif operations[i]== "X--":
                ans-=1
            else :
                ans+=1
        return ans
