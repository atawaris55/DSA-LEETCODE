class Solution(object):
    def wordPattern(self, pattern, s):
        mapping={}
        reverse={}
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for x,y in zip(pattern,words):
            if x not in mapping:
                mapping[x]=y
            elif mapping[x]!=y:
                return False
            if y not in reverse:
                reverse[y]=x
            elif reverse[y]!=x:
                return False
        return True