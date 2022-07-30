from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid) 
        N = len(grid[0])
        
        visits = [[False] * N for _ in range(M)]
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        """
        Use dfs function for all nodes if it is land
        Check whether the result is True!
        """
        
        def dfs(x, y, grid):
            """
            If visit -> continue 
            Else -> change visit, and go more
            """
            
            if visits[x][y] :   return False
            
            visits[x][y] = True
            condition = False
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=M or ny>= N : continue 
                if visits[nx][ny] or grid[nx][ny] == "0" : continue 
                dfs(nx,ny,grid)
            return True
        
        islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]== "1":
                    if dfs(i,j,grid):
                        print("i,j:", (i,j))
                        islands +=1 
        return islands
            
                
s = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(s.numIslands(grid))