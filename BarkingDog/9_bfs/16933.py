#16933. 벽 부수고 이동하기 3
"""
벽뿌이의 확장 버전.
"""

import sys 
input = sys.stdin.readline
from collections import deque

N,M,K = map(int,input().rstrip().split())
dist = [[[[-1] * M for _ in range(N)] for _ in range(K+1)] for _ in range(2)]

boards = []
for _ in range(N):
    boards.append(list(map(int,list(input().rstrip()))))
    
#시작점 처리
deq = deque([(0,0,0, True)])
dist[1][0][0][0] = 0

dx = [-1,1,0,0,0]
dy = [0,0,-1,1,0]

def bfs(deq):
    global dist
    while deq:
        drill, cur_x,cur_y, flag = deq.popleft()    
        # print(f"drill : {drill}, cur_x:{cur_x}, cur_y:{cur_y}, flag:{flag}, dist: { dist[flag][drill][cur_x][cur_y] }")
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]   
            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if dist[not flag][drill][nx][ny]>=0 : 
                continue    
                
            #일반적인 이동
            if boards[nx][ny] == 0:
                dist[not flag][drill][nx][ny] = dist[flag][drill][cur_x][cur_y]+1
                deq.append((drill,nx,ny, not flag))
                
                
            #벽을 부수는 이동
            if drill<K and boards[nx][ny] == 1: #부술 수 있다면                     
                if flag:
                    if dist[not flag][drill+1][nx][ny]>=0 : continue
                    dist[not flag][drill+1][nx][ny] = dist[flag][drill][cur_x][cur_y]+1
                    deq.append((drill+1, nx,ny, not flag))
                else:         
                    if dist[flag][drill+1][nx][ny]>=0 : continue
                    dist[flag][drill+1][nx][ny] = dist[flag][drill][cur_x][cur_y]+2
                    deq.append((drill,nx,ny,flag))
                    
                    
    candidates = [dist[0][drill][N-1][M-1] for drill in range(K+1) if dist[0][drill][N-1][M-1]>-1]
    candidates.extend([dist[1][drill][N-1][M-1] for drill in range(K+1) if dist[1][drill][N-1][M-1]>-1])
    # print("candidates:", candidates)
    if not candidates: 
        answer = -1 
    else:
        answer = min(candidates)+1
    return answer
        
print(bfs(deq))