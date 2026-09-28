class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        res = nums1 + nums2
        res.sort()
        n = len(res)

        if n % 2 == 0:
            return float(res[(n//2)-1] + res[n//2]) / 2
        else:
            return res[n//2]