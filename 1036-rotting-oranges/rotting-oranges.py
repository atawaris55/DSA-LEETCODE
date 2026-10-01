from collections import deque
from copy import deepcopy
class Solution(object):
    def orangesRotting(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        fresh_ct=0
        minutes=0
        queue=deque()
        grid_cp=deepcopy(grid)
        for r in range(rows):
            for c in range(cols):
                if grid_cp[r][c]==2:
                    queue.append((r,c))
                elif grid_cp[r][c]==1:
                    fresh_ct+=1
        while queue and fresh_ct>0:
            minutes+=1
            total_rotten=len(queue)
            for _ in range(total_rotten):
                i,j=queue.popleft()
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_i,new_j=i+dx,j+dy
                    if new_i<0 or new_j<0 or new_i==rows or new_j==cols:
                        continue
                    if grid_cp[new_i][new_j]==0 or grid_cp[new_i][new_j]==2:
                        continue
                    fresh_ct -=1
                    grid_cp[new_i][new_j]=2
                    queue.append((new_i,new_j))
        if fresh_ct>0:
            return -1
        return minutes