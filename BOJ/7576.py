#7576. 토마토
"""
바킹독 BFS 연습문제 3 :: 토마토

만약 출발점이 여러 개라면 어떻게 해야할까?
"""

import sys
input = sys.stdin.readline
from collections import deque


M,N = map(int,input().rstrip().split())
board = []
initials = deque([]) #익은 토마토가 들어있는 위치를 저장할 배열
not_tomatoes = 0 #처음부터 안익은 것들을 세기 위함
for row in range(N):
    rows= list(map(int,input().rstrip().split()))
    board.append(rows)
    for col in range(M):
        if rows[col] == 1 :
            initials.append((row,col))
        elif rows[col] == -1:
            not_tomatoes +=1
dist = [[0] * M for _ in range(N)] #몇 칸을 지나야하는지에 대한 배열


#BFS 하는 함수(dist matrix는 계속 공유해서 쓸 것이므로, 전역변수로 이용하자.)


def bfs(deq):
    tomatoes = 0
    result = 0
    dx = [1,-1,0,0] 
    dy = [0,0,1,-1]
    while deq:
        cur_x, cur_y = deq.popleft()
        result = dist[cur_x][cur_y] #계속 갱신되겠지
        tomatoes +=1 #토마토의 개수! pop될때마다 세면 되겠지
        for i in range(4):
            nx= cur_x + dx[i] ; ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M : continue #범위 out 
            if dist[nx][ny]>0 or board[nx][ny] != 0: continue #방문할 필요 없는 곳
            dist[nx][ny] = dist[cur_x][cur_y] + 1
            deq.append((nx,ny))
    return result, tomatoes
#이제 모든 node에 대해 방문해보자
max_day, bfs_tomatoes = bfs(initials)

print(max_day if bfs_tomatoes == N*M- not_tomatoes else -1)