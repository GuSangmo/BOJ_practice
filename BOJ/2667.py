#2667. 단지번호 붙이기 
"""
FLood fill의 예시
"""

import sys 
input = sys.stdin.readline
from collections import deque 

N = int(input().rstrip())
boards = [list(input().rstrip()) for _ in range(N)]
visits = [[False for _ in range(N)] for _ in range(N)]
def bfs(start, board):
    start_x, start_y = start
    deq = deque([start])
    size = 0
    visits[start_x][start_y] = True
    while deq:
        cur_x, cur_y = deq.popleft()
        size +=1
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx< 0 or ny <0 or nx>=N or ny>= N : continue 
            if boards[nx][ny] == "0": continue 
            if visits[nx][ny] : continue 
            visits[nx][ny] = True 
            deq.append((nx,ny))
    return size

villages = []
for row in range(N):
    for col in range(N):
        if boards[row][col] == "1" and not visits[row][col]:
            size = bfs( (row,col), boards)
            villages.append(size)
print(len(villages))


print(*sorted(villages), sep= "\n")