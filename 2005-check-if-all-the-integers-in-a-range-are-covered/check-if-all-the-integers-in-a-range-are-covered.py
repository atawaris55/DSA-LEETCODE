class Solution(object):
    def isCovered(self, ranges, left, right):
        for i in range(left,right+1):
            covered=False
            for r in ranges:
                if r[0]<=i<=r[1]:
                    covered=True
                    break
            if covered==False:
                return False
        return True