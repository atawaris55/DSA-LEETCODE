class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        g=list(words)
        g=g[::-1]
        return " ".join(g )