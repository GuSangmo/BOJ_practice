#2146.다리 만들기

"""
여러 개의 섬을 bfs를 이용해 numbering 한후, 개별적인 걸 deq에 담는다!
그 후 각 섬에서 다른 섬까지의 최단거리를 구한다.

여기서의 issue: 
dist array를 반복적으로 수정할시 그걸 global하게 공유한다. 
따라서 함수에서 array를 개별적으로 수정헀음.

시간은 그렇다 치고 memory error뜰까 두렵다.

"""

import sys
input = sys.stdin.readline
from collections import deque


#1. I/O 처리
N = int(input().rstrip())
board = [list(map(int,input().rstrip().split())) for _ in range(N)]
islands = [[0] * N for _ in range(N)]
visit = [[0] * N for _ in range(N)]
                  

#2. BFS logic 
"""
같은 구역일때만 세어서, 새로운 islands array를 만듬.

O(N^2) : islands를 만드는 데 걸리는 시간
"""

def bfs(x,y, value):
    deq = deque([(x,y)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0        
    visit[x][y] = 1
    islands[x][y] = value
    while deq:
        cur_x, cur_y = deq.popleft() ; cnt+=1
        for i in range(4):
            nx = cur_x+dx[i] ; ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny >=N : continue
            if visit[nx][ny] : continue #이미 방문한 곳
            if not board[nx][ny] : continue
            visit[nx][ny] = 1
            deq.append((nx,ny))
            islands[nx][ny] = value
    return True if cnt>0 else False

num_islands = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visit[i][j]:
            bfs(i,j, num_islands+1)
            num_islands+=1

"""
islands를 훑으면서 각 섬들의 위치가 담긴 위치를 저장한다.
"""

locs ={i:list() for i in range(1,num_islands+1)}
for i in range(N):
    for j in range(N):
        if islands[i][j]==0:continue
        k = islands[i][j]
        locs[k].append((i,j))

"""
이제 각각의 섬에서 다른 곳까지의 거리를 구하자!
"""
dist = [[-1] * N for _ in range(N)]
def get_min_dist_bfs(start_island):
    dist = [[-1] * N for _ in range(N)]
    deq = deque(locs[start_island])
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while deq:
        cur_x, cur_y = deq.popleft()
        if islands[cur_x][cur_y] == start_island : dist[cur_x][cur_y] = 0        
        if islands[cur_x][cur_y]!= 0 and islands[cur_x][cur_y] != start_island : 
            return dist[cur_x][cur_y]-1
        for i in range(4):
            nx = cur_x+dx[i] ; ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny >=N : continue
            if dist[nx][ny]>=0 : continue #이미 방문한 곳

            
            dist[nx][ny] = dist[cur_x][cur_y]+1
            deq.append((nx,ny))
    

minimum = 1e5
for start in range(1,num_islands+1):
    minimum = min(minimum, get_min_dist_bfs(start))
print(minimum)

    
