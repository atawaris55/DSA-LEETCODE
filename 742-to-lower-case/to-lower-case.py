class Solution(object):
    def toLowerCase(self, s):
        m=''
        for ch in s:
            m+=ch.lower()
        return m