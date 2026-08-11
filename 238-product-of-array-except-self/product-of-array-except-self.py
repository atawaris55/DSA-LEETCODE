class Solution(object):
    def productExceptSelf(self, nums):
        ans=[]
        pro=1
        zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
   
                zeros+=1
            else:
                pro*=nums[i]

        for i in range(len(nums)):
            if zeros>1:
                ans.append(0)
            elif zeros==1:
                if nums[i]==0:
                    ans.append(pro)
                else:
                    ans.append(0)
            else:
                val=pro//nums[i]
                ans.append(val)
        return ans

            