class Solution(object):
    def minOperations(self, s):
        if list(s)==sorted(s):
            return 0
        if len(s)==2:
            return -1
        mini=min(s)
        maxi=max(s)
        if mini==s[0] or maxi==s[-1]:
            return 1
        if mini in s[1:-1] or maxi in s[1:-1]:
            return 2
        return 3