class Solution(object):
    def strStr(self, haystack, needle):
        ls=[]
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                ls.append(i)
        if len(ls)>0:
            return ls[0]
        else:
            return -1
