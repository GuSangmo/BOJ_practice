#7562. 나이트의 이동

"""
나이트를 그냥 이동시키면 된다
"""

import sys
input = sys.stdin.readline
from collections import deque


#1. I/O 처리

def bfs(start, target, dist):
    global board #밑에서 정의할 것
    N = len(dist)
    dx = [1,1,-1,-1,2,2,-2,-2]
    dy = [2,-2,2,-2,1,-1,1,-1]
    sx, sy = start 
    ex, ey = target
    deq = deque([start])
    dist[sx][sy] = 0
    while deq:
        cur_x, cur_y = deq.popleft()
        if cur_x == ex and cur_y == ey:
            return dist[cur_x][cur_y]
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx< 0 or ny< 0 or nx>=N or ny>=N : continue
            if dist[nx][ny]>=0 : continue
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            deq.append((nx,ny))

T = int(input().rstrip())
for _ in range(T):
    l = int(input().rstrip())
    board = [[0] * l for _ in range(l)]
    dist = [[-1] * l for _ in range(l)]
    sx, sy = map(int,input().rstrip().split())
    ex, ey = map(int,input().rstrip().split())
    result = bfs((sx,sy), (ex,ey), dist)
    print(result)     



