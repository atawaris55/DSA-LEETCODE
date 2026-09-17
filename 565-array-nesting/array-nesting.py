class Solution(object):
    def arrayNesting(self, nums):
        visited=set()
        max_count=0
        for i in range(len(nums)):
            if i in visited:
                continue
            curr=i
            count=0
            while curr not in visited:
                visited.add(curr)
                curr=nums[curr]
                i+=1
                count+=1
            max_count=max(max_count,count)
        return max_count
