class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        moves=0
        for i in range(len(arr1)):
            valid=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    valid=False
                    break
            if valid:
                moves+=1
                
        return moves
                