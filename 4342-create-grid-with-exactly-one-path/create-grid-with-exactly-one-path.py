class Solution(object):
    def createGrid(self, m, n):
        ans=[]
        grid=[['#']*n for _ in range(m)]
        for j in range(n):
            grid[0][j]='.'
        for i in range(m):
            grid[i][n-1]='.'
            print(grid)
        for v in grid:
            ans.append("".join(v))
        return ans
