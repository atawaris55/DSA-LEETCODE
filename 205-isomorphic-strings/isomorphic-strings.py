class Solution(object):
    def isIsomorphic(self, s, t):
        mapping={}
        reverse={}
        for x,y in zip(s,t):
            if x not in mapping:
                mapping[x]=y
            elif mapping[x]!=y:
                return False
            if y not in reverse:
                reverse[y]=x
            elif reverse[y]!=x:
                return False

        return True
