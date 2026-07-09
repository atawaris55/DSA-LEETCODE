class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        total=0
        def backrack(idx,total,subset):
            if total==target:
                res.append(subset[:])
                return
            elif total>target:
                return
            if idx>=len(candidates):
                return 
            subset.append(candidates[idx])
            backrack(idx, total + candidates[idx], subset)
            subset.pop()
            backrack(idx + 1, total, subset)
        backrack(0,0,[])
        return res


