class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = []
        operations = k1 + k2

        for i in range(len(nums1)):
            diff.append(abs(nums1[i] - nums2[i]))

        if operations >= sum(diff):
            return 0

        highest = max(diff)
        count = [0] * (highest + 1)

        for x in diff:
            count[x] += 1

        for i in range(highest, 0, -1):
            if operations == 0:
                break

            if operations >= count[i]:
                operations -= count[i]
                count[i - 1] += count[i]
                count[i] = 0
            else:
                count[i] -= operations
                count[i - 1] += operations
                operations = 0
                break

        ans = 0

        for i in range(len(count)):
            ans += i * i * count[i]

        return ans