class Solution(object):
    def maxScore(self, cardPoints, k):
        left_sum,right_sum=0,0
        for i in range(k):
            left_sum+=cardPoints[i]
        maxi=left_sum
        right_idx=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_idx]
            maxi=max(maxi,right_sum+left_sum)
            right_idx-=1
        return maxi
