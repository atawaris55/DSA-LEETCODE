class Solution(object):
    def generateParenthesis(self, n):
        brackets = [""] * (n*2)
        res = []

        def solve(idx, total, open_count):
            if idx == len(brackets):
                if total == 0:
                    res.append("".join(brackets))
                return

   
            if open_count < n:
                brackets[idx] = "("
                solve(idx+1, total+1, open_count+1)


            if total > 0:
                brackets[idx] = ")"
                solve(idx+1, total-1, open_count)

        solve(0,0,0)

        return res