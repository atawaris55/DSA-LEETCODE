class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        for i in range(len(words)):
            char=list(words[i])

            left=0
            right=len(char)-1
            while left<right:
                char[left],char[right]=char[right],char[left]
                left+=1
                right-=1
            words[i] = ''.join(char)
        return ' '.join(words)
