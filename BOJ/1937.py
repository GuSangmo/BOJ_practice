#1937. 욕심쟁이 판다
"""
대나무가 더 많은 곳으로 이동하는 판다.
최단 경로가 아니다. 따라서 DFS.
모든 곳에서의 출발 정보가 필요한데, 그러면 TLE가 뜰 것이다 ==> DP
"""

import sys 
sys.setrecursionlimit(100_000_0)
input = sys.stdin.readline 
N = int(input().rstrip())
forests = [list(map(int,input().rstrip().split())) for _ in range(N)]

#dp[row][col] ==> (row,col)에서 이동 가능한 최대 칸의 개수

dp = [[0 for _ in range(N)] for _ in range(N)]
visits = [[False for _ in range(N)] for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
maximum = -1
def dfs(row,col):
    global maximum
    #If already done, use caching
    if dp[row][col] > 0 :
        maximum = max(maximum, dp[row][col])
        return dp[row][col]
    dp[row][col] = 1
    visits[row][col] = True  #방문처리
    for i in range(4):
        next_row = row + dx[i]
        next_col = col + dy[i]
        if next_row <0 or next_col < 0 or next_row >=N or next_col >=N : continue 
        if visits[next_row][next_col] : continue 
        if forests[next_row][next_col] <= forests[row][col]:
            dp[row][col] = max(dp[row][col], 1 + dfs(next_row, next_col))
        
    visits[row][col] = False 
    return dp[row][col]

answer = -1
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i,j))

print(answer)


