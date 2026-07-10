class Solution(object):
    def topKFrequent(self, nums, k):
        seen={}
        res=[]
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        arr= sorted(seen.items(), key= lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(arr[i][0])
        return res
            

