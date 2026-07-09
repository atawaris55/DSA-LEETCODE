class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(idx, target, subset):
            if target == 0:
                res.append(subset[:])
                return

            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    continue

                subset.append(candidates[i])

                # same element can be picked again
                backtrack(i, target - candidates[i], subset)

                subset.pop()

        backtrack(0, target, [])
        return res