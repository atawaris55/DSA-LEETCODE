class Solution(object):
    def majorityElement(self, nums):

        n=len(nums)//3
        res=[]
        element_count = Counter(nums)
        for k,val in element_count.items():
            if val>n:
                res.append(k)
        return res
                