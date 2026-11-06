class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        q = sorted((time, i) for i, time in enumerate(queries))

        count = {}
        ans = [0] * len(queries)

        left = 0
        right = 0

        for time, idx in q:
            start = time - x

            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]

                count[server] = count.get(server, 0) + 1
                right += 1

            while left < len(logs) and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans