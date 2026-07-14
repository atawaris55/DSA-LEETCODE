class Solution(object):
    def removeOuterParentheses(self, s):
        count=0
        done=[]
        for ch in s:
            if ch=='(':
                if count>0:
                    done.append(ch)
                count+=1
            else:
                count-=1
                if count>0:
                    done.append(ch)
        return "".join(done)




