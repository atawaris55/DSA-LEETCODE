class Solution(object):
    def maxLength(self, nums):
        ans=0
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        for i in range(len(nums)):
            pro=1
            lcm_val=1
            gcd_val=0
            for j in range(i,len(nums)):
                pro*=nums[j]
                
                gcd_val=gcd(gcd_val,nums[j])
                lcm_val=(lcm_val*nums[j])//gcd(lcm_val,nums[j])
                if pro==gcd_val*lcm_val:
                    ans=max(ans,j-i+1)
        return ans

                
