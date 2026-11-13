class Solution(object):
    def mostWordsFound(self, sentences):
        ans=0
        for i in range(len(sentences)):
            ans=max(ans,len(sentences[i].split()))

        return ans

