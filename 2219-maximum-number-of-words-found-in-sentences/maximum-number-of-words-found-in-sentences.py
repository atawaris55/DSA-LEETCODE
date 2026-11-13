class Solution(object):
    def mostWordsFound(self, sentences):
        ans=len(sentences[0].split())
        for i in range(len(sentences)):
            ans=max(ans,len(sentences[i].split()))
        print(ans)
        return ans

