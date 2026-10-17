class Solution(object):
    def minSwaps(self, nums):
        arr = []
        for i, n in enumerate(nums):
            s = 0
            x = n
            while x:
                s += x % 10
                x //= 10
            arr.append((s, n, i))

        arr.sort()
        visited = [False] * len(nums)
        count = 0

        for i in range(len(nums)):
            if visited[i] or arr[i][2] == i:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle += 1

            count += cycle - 1

        return count