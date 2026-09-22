class Solution(object):
    def longestMountain(self, arr):
        maxi=0
        res=0
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                left=right=i
                while left>0 and arr[left-1]<arr[left]:
                    left-=1
                    
                while right<len(arr)-1 and arr[right]>arr[right+1]:
                    right+=1
                res=right-left+1
                maxi=max(maxi,res)
        return maxi