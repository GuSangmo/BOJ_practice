#1937. 욕심쟁이 판다
"""
대나무를 좋아하는 판다는, 계속 무언가를 먹어치움
근처로 움직이려면 더 많이 먹어야 함

Fail 1. 단순 BFS/DFS를 돌리면 모든 점을 시작점으로 돌아야 하기 때문에, 2500,000 **2 ==> TLE.

Fail 2. 따라서 DFS로 한번 다 돈 후 -> 이미 업데이트된것들은 DP로 탐색시간을 줄여야 한다.


"""

import sys 
from collections import deque
sys.setrecursionlimit(100_000_0)
input = sys.stdin.readline 
N = int(input().rstrip())
bamboos = [list(map(int,input().rstrip().split())) for _ in range(N)]
paths = [[0 for _ in range(N)] for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(row,col):
    if paths[row][col] > 0 :
        return paths[row][col]    
    paths[row][col] = 1
    for idx in range(4):
        tmp_row = row + dx[idx]
        tmp_col = col+ dy[idx]
        if tmp_row <0 or tmp_col < 0 or tmp_row >=N or tmp_col >= N : continue
        if bamboos[tmp_row][tmp_col] <= bamboos[row][col] : continue 
        paths[row][col] = max(paths[row][col], dfs(tmp_row,tmp_col)+1 )
    return paths[row][col]

answer = 1
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i,j))

print(answer)