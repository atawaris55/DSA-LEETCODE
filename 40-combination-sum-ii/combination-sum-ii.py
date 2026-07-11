class Solution(object):
    def combinationSum2(self, candidates, target):
        n=len(candidates)
        candidates.sort()
        res=[]
        def backtrack(idx,total,subset):
            if total==0:
                res.append(subset[:])
                return
            if total<0:
                return
            if idx>=n:
                return
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                subset.append(candidates[i])
                summ=total-candidates[i]
                backtrack(i+1,summ,subset)
                subset.pop()
        backtrack(0,target,[])
        return res