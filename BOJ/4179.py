#4179. 불
"""
바킹독 BFS 연습문제 4 :: 불!

두 개의 BFS 조건을  지정하기!

Checkpoint

1:: 불은 여러개일 수 있으므로, 입력단에서 큐에 넣어두고 이를 처리

2:: 불은 없을 수 있으므로, 불의 BFS처리 과정에서 이를 처리


"""

import sys
input = sys.stdin.readline
from collections import deque

#Part 1 :: 입력 처리

R,C = map(int,input().rstrip().split())
mazes = []
fire_start = deque([])

fire_dist = [[-1] * C for _ in range(R)]
jihoon_dist = [[-1] * C for _ in range(R)]


for row in range(R):
    rows= list(input().rstrip())
    mazes.append(rows)
    for col in range(C):
        if rows[col] == "#" :  
            mazes[row][col] = 0 #벽은 이렇게 처리!
        elif rows[col] == ".": 
            mazes[row][col] = 1
        elif rows[col] == "F":
            fire_dist[row][col] = 0
            fire_start.append((row,col))
            mazes[row][col] = 1
        elif rows[col] == "J":
            jihoon_start = (row,col)
            mazes[row][col] = 1

#Part 2 :: BFS 처리






#불의 위치가 정의되었을때 bfs를 할 수 있다.
def fire_bfs(deq, dist):
    """
    불 시작위치가 담긴 deq로 BFS 지정!.
    """
    #이미 초깃값들을 채워놓았음.
    if not deq: return dist    
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1]
    while deq:
        cur_x, cur_y = deq.popleft()
        result = dist[cur_x][cur_y] #계속 갱신되겠지
        for i in range(4):
            nx= cur_x + dx[i] ; ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=R or ny>=C : continue
            if dist[nx][ny]>=0 or mazes[nx][ny] == 0: continue #방문할 필요 없는 곳
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            deq.append((nx,ny))
    return dist    


def jihoon_bfs(start, dist, fire_array):    
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1]
    jihoon_x, jihoon_y = start
    dist[jihoon_x][jihoon_y] = 0
    deq= deque([(jihoon_x,jihoon_y)])
    while deq:
        cur_x, cur_y = deq.popleft()
      #  print("cur_x,cur_y:", (cur_x,cur_y))
        result = dist[cur_x][cur_y] #계속 갱신되겠지
        for i in range(4):
            nx= cur_x + dx[i] ; ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=R or ny>=C : 
                possible= dist[cur_x][cur_y] + 1
                return possible
            if dist[nx][ny]>=0 or mazes[nx][ny] == 0: continue #방문할 필요 없는 곳    
            #불이 타는 경우는 제외!
            if dist[cur_x][cur_y] + 1 >= fire_array[nx][ny] and fire_array[nx][ny]!= -1 : 
                continue #불타오르네     
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            deq.append((nx,ny))
    return "IMPOSSIBLE"



fire_array = fire_bfs(fire_start, fire_dist)
escape_time = jihoon_bfs(jihoon_start, jihoon_dist, fire_array)

print(escape_time)


