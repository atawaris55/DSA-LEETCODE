class Solution(object):
    def checkIfPangram(self, sentence):
        arr=[0]*26
        for ch in sentence:
            arr[ord('a')-ord(ch)]=1
        for i in arr:
            if i==0:
                return False
        return True