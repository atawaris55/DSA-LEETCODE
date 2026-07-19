class Solution(object):
    def isValid(self, s):
        a=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=="[":
                a.append(ch)

            else:
                if not a:
                    return False
                top=a.pop()
                if ch==')' and top!='(':
                    return False
                if ch=='}' and top!='{':
                    return False
                if ch==']' and top!='[':
                    return False
        return len(a)==0
    