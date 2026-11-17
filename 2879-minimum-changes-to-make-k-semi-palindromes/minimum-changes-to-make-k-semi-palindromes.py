
class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        # Precompute minimum changes for each substring
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = float('inf')

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    m = length // d

                    for r in range(d):
                        for x in range(m // 2):
                            a = i + r + x * d
                            b = i + r + (m - 1 - x) * d

                            if s[a] != s[b]:
                                changes += 1

                    best = min(best, changes)

                cost[i][j] = best

        # DP
        dp = [[float('inf')] * (n + 1)
              for _ in range(k + 1)]

        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
