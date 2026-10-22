class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        indx0 = nums.index(0)

        def is_increasing():
            for i in range(n):
                if nums[(i + 1) % n] != (nums[i] + 1) % n:
                    return False
            return True

        def is_decreasing():
            for i in range(n):
                if nums[(i + 1) % n] != (nums[i] - 1 + n) % n:
                    return False
            return True

        best = float('inf')

        if is_increasing():
            best = min(best, indx0, (n - indx0) + 2)

        if is_decreasing():
            best = min(best, indx0 + 2, n - indx0)

        return best if best != float('inf') else -1
        