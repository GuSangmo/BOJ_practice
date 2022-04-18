#2583. 영역 구하기
"""
K개의 input에 대해 bfs를 실시하여 1로 만든 후 loop를 돌면 된다.

최대 10000번 갱신. 10000 * 100 = 100만이라 시간이 오래 걸리지 않을 것. 

좌표는 기울여서 생각하자!

갱신이 안되었던 이유는 deep copy때문이었음... 

"""

import sys 
input = sys.stdin.readline 
M,N,K = map(int,input().rstrip().split())
from collections import deque


boards = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    s_x, s_y, e_x, e_y = map(int,input().rstrip().split())
    for x in range(s_x,e_x):
        for y in range(s_y,e_y):
            boards[x][y] = 1
            
#Flood fill 
visit = [[0] * M for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    if visit[x][y] : return False,0
    area_size = 0
    deq = deque([(x,y)])
    while deq:
        cur_x, cur_y = deq.popleft()
        visit[cur_x][cur_y] = 1
        area_size +=1 
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M : continue 
            if visit[nx][ny]: continue
            if boards[nx][ny] == 1 : continue
            visit[nx][ny] = 1
            deq.append((nx,ny))
    return True , area_size    

total_zone = 0
total_areas = []
for i in range(N):
    for j in range(M):
        if boards[i][j] : continue 
        alreayVisit, area_cnt = bfs(i,j)
        if alreayVisit: 
            total_zone+=1 
            total_areas.append(area_cnt)
print(total_zone)
total_areas.sort()
print(*total_areas, sep = " ")
