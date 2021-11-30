#10026. 적록색약
"""
일반인과 적록색약을 구분해서 센다!
"""

import sys
input = sys.stdin.readline
from collections import deque


#1. I/O 처리
N = int(input().rstrip())
original_board = []
redgreen_board = []
original_visit = [[0] * N for _ in range(N)]
redgreen_visit = [[0] * N for _ in range(N)]

for row in range(N):
    rows = list(input().rstrip())
    arr = []
    arr2 = []
    for col in range(N):
        if rows[col] == "R":
            arr.append(1)
            arr2.append(1)
        elif rows[col] == "G":
            arr.append(2)
            arr2.append(1)
        else:
            arr.append(3)
            arr2.append(3)
    original_board.append(arr)
    redgreen_board.append(arr2)
    
#2. BFS logic 
"""
같은 구역일때만 센다.
"""

def bfs_original(x,y):
    deq = deque([(x,y)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0        
    original_visit[x][y] = 1
    while deq:
        cur_x, cur_y = deq.popleft() ; cnt+=1
        for i in range(4):
            nx = cur_x+dx[i] ; ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny >=N : continue
            if original_visit[nx][ny] : continue #이미 방문한 곳
            if original_board[nx][ny] != original_board[cur_x][cur_y] : continue
            original_visit[nx][ny] = 1
            deq.append((nx,ny))
    return True if cnt>0 else False

def bfs_redgreen(start):
    deq = deque([start])
    x, y = start
    
    redgreen_visit[x][y] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0
    while deq:
        cur_x, cur_y = deq.popleft() ; cnt+=1
        for i in range(4):
            nx = cur_x+dx[i] ; ny = cur_y + dy[i]  
            if nx<0 or ny<0 or nx>=N or ny >=N : continue
            if redgreen_visit[nx][ny] : continue
            if redgreen_board[nx][ny] != redgreen_board[cur_x][cur_y] : continue
            redgreen_visit[nx][ny] = 1
            deq.append((nx,ny))
    return True if cnt>0 else False


result1 = 0 ; result2 = 0
for i in range(N):
    for j in range(N):
        ans1 = int(bfs_original(i,j)) if not original_visit[i][j] else 0
        ans2 = int(bfs_redgreen((i,j))) if not redgreen_visit[i][j] else 0
        result1 +=ans1
        result2 +=ans2        
print(result1, result2)