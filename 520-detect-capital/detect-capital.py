class Solution(object):
    def detectCapitalUse(self, word):
        upr=0
        for ch in word:
            if ch.isupper():
                upr+=1
        if upr==len(word):
            return True
        if upr==0:
            return True
        if word[0].isupper() and upr==1:
            return True
        else:
            return False



            
