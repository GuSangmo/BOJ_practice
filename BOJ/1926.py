#1926. 그림
"""
바킹독 BFS 연습문제 1 :: 길이가 0인 것도 신경쓰자!
"""

import sys
input = sys.stdin.readline
from collections import deque


n,m = map(int,input().rstrip().split())
board = [list(map(int,input().rstrip().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
num_pics = 0

#BFS 하는 함수(visit matrix는 계속 공유해서 쓸 것이므로, 전역변수로 이용하자.)
def bfs(start):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    deq = deque([])
    deq.append(start)
    picture_size = 0
    while deq:
        cur_x, cur_y = deq.pop() ; picture_size +=1
        visit[cur_x][cur_y]= 1
        
        for i in range(4):
            nx= cur_x + dx[i] ; ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m : continue #범위 out 
            if visit[nx][ny] or board[nx][ny] == 0: continue #방문할 필요 없는 곳
            visit[nx][ny] = 1
            deq.append((nx,ny))
    return picture_size

#이제 모든 node에 대해 방문해보자
board_sizes = []
for row in range(n):
    for col in range(m):
        #여기서 시작점부터 후보가 안되면 사전처리해준다.
        if visit[row][col] or board[row][col] ==0 : continue
        result = bfs((row,col))
        board_sizes.append(result)
        num_pics += int(result>0)
         
print(num_pics)
print(max(board_sizes) if board_sizes else 0)

