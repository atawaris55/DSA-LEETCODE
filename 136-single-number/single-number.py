class Solution(object):
    def singleNumber(self, nums):
        my_dict={}
        for num in nums:
            if num in my_dict:
                my_dict[num]+=1
            else:
                my_dict[num]=0
        for key,val in my_dict.items():
            if val==0:
                return key

