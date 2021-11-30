#5427. 불

"""
불이 전파 안되는 경우, 여러 개인 경우도 고려해서 코드를 짜자!
"""

import sys
input = sys.stdin.readline
from collections import deque

# BFS

def fire_bfs(deq, dist):    
    if not deq : return dist  #불이 나는 지점이 없다면, 그대로 return
    global board
    N = len(dist)
    M = len(dist[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while deq:
        cur_x, cur_y = deq.popleft()        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx< 0 or ny< 0 or nx>=N or ny>=M: continue 
            if dist[nx][ny]>=0 or board[nx][ny] == 0: continue
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            deq.append((nx,ny))
    return dist
    
def human_bfs(deq,dist, fire_array):
    """
    logic : 갱신하기 전에 nx,ny값을 함부로 비교하면 안 돼!
    """
    global board
    N = len(dist)
    M = len(dist[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while deq:
        cur_x, cur_y = deq.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx< 0 or ny< 0 or nx>=N or ny>=M: 
                return dist[cur_x][cur_y]+1 
            if dist[nx][ny]>=0 or board[nx][ny] == 0: continue                
            if fire_array[nx][ny]!= -1 and dist[cur_x][cur_y]+1>=fire_array[nx][ny] : continue
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            deq.append((nx,ny))

    
    return "IMPOSSIBLE"
    
#Input/Output 처리
T = int(input().rstrip())
for _ in range(T):
    w, h = map(int,input().rstrip().split())
    board = [list(input().rstrip()) for _ in range(h)]
    fire_deq = deque([])
    fire_dist = [[-1] * w for _ in range(h)]
    human_dist = [[-1] * w for _ in range(h)]
    
    #board 갱신 
    for row in range(h):
        for col in range(w):
            if board[row][col] == "." :
                board[row][col] = 1
            elif board[row][col] == "#":
                board[row][col] = 0
            elif board[row][col] == "@":
                board[row][col] = 1
                human_deq = deque([(row,col)])
                human_dist[row][col] = 0
            elif board[row][col] == "*":
                board[row][col] = 1
                fire_dist[row][col] = 0
                fire_deq.append((row,col))

    fire = fire_bfs(fire_deq, fire_dist)    
    result = human_bfs(human_deq, human_dist, fire)
    print(result)

