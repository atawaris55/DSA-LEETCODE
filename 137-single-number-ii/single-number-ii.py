class Solution(object):
    def singleNumber(self, nums):
        seen=[]
        seen1=set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                seen1.add(nums[i])
        seen_sum=sum(seen)
        seen1_sum=sum(seen1)
        return seen_sum-seen1_sum