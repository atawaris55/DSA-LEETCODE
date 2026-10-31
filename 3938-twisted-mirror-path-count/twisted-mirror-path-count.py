
class Solution(object):
    def uniquePaths(self, grid):
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7

        vornadexil = grid

        dp = [[[0, 0] for j in range(n)] for i in range(m)]

        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):

                for d in range(2):

                    ways = dp[i][j][d]

                    if ways == 0:
                        continue

                    if grid[i][j] == 0:

                        if j + 1 < n:
                            dp[i][j+1][0] = (dp[i][j+1][0] + ways) % mod

                        if i + 1 < m:
                            dp[i+1][j][1] = (dp[i+1][j][1] + ways) % mod

                    else:

                        if d == 0 and i + 1 < m:
                            dp[i+1][j][1] = (dp[i+1][j][1] + ways) % mod

                        elif d == 1 and j + 1 < n:
                            dp[i][j+1][0] = (dp[i][j+1][0] + ways) % mod

        return (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % mod
