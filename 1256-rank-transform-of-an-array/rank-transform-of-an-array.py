class Solution(object):
    def arrayRankTransform(self, arr):
        ans=[]
        sorted_arr=sorted(arr)
        rank={}
        rankin=1
        for num in sorted_arr:
            if num not in rank:
                rank[num]=rankin
                rankin+=1
        for num in arr:
            if num in rank:
                ans.append(rank[num])
        return ans