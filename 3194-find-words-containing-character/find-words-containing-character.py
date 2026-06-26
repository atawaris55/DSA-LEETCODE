class Solution(object):
    def findWordsContaining(self, words, x):
        res=[]
        for i,word in enumerate(words) :
            for ch in word:
                if ch==x:
                    res.append(i)
                    break
        return res
