#14442. 벽 부수고 이동하기 2
"""
벽뿌이의 확장 버전.
"""

import sys 
input = sys.stdin.readline
from collections import deque

N,M,K = map(int,input().rstrip().split())
dists = [[[-1] * M for _ in range(N)] for _ in range(K+1)]

boards = []
for _ in range(N):
    nums = list(input().rstrip())
    boards.append(list(map(int,nums)))

    
#시작점 처리
deq = deque([(0,0,0)])
dists[0][0][0] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start, dist,deq):    
    while deq:
        drill, cur_x,cur_y = deq.popleft()        
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]         
            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if dist[drill][nx][ny]>=0 : continue
            if boards[nx][ny] == 0:
                dist[drill][nx][ny] = dist[drill][cur_x][cur_y]+1
                deq.append((drill,nx,ny))    
            if drill<K and boards[nx][ny] == 1 : #부숴야한다면 
                if dist[drill+1][nx][ny]>=0 : continue 
                dist[drill+1][nx][ny] = dist[drill][cur_x][cur_y]+1
                deq.append((drill+1, nx,ny))
    candidates = [dist[drill][N-1][M-1] for drill in range(K+1) if dist[drill][N-1][M-1]>-1]
    
    if not candidates: 
        answer = -1 
    else:
        answer = min(candidates)+1
    return answer
        
print(bfs((0,0,0) , dists, deq))