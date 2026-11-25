
class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        def check(length):
            count = {}

            h = 0
            base = 131
            mod = 10**9 + 7
            power = pow(base, length, mod)

            for i in range(length):
                h = (h * base + nums[i]) % mod

            count[h] = 1

            for i in range(length, n):
                h = (h * base - nums[i-length] * power + nums[i]) % mod
                count[h] = count.get(h, 0) + 1

            return any(v == 1 for v in count.values())

        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
