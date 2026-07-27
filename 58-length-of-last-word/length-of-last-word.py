class Solution(object):
    def lengthOfLastWord(self, s):
        g=[]
        for word in s.split():
            g.append(word)
        return len(g[-1])
