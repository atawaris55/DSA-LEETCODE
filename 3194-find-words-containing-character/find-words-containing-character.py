class Solution(object):
    def findWordsContaining(self, words, x):
        res=set()
        for i,word in enumerate(words) :
            for ch in word:
                if ch==x:
                    res.add(i)
        return list(res)
