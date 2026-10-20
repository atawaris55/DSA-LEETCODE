class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)

        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        D = [0] * n
        for i in range(1, n):
            D[i] = D[i - 1] + (1 if nums[i - 1] > nums[i] else 0)

        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            m = n // k
            valid = True

            # value-range check between blocks
            for b in range(1, m):
                r = b * k
                if pref_max[r] > suff_min[r]:
                    valid = False
                    break

            # per-block CYCLIC break check (this was the missing part)
            if valid:
                for l in range(0, n, k):
                    r = l + k
                    internal = D[r - 1] - D[l]
                    wrap = 1 if nums[r - 1] > nums[l] else 0
                    if internal + wrap > 1:
                        valid = False
                        break

            if valid:
                total += k

        return total