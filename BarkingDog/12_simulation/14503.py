#14503. 로봇 청소기
"""뱀과 비슷한 문제.
회전방향을 잘만 구현하면 괜찮을 것 같다.

O(NM)을 DFS해야 하니 시간은 충분할 것 같다.
"""

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from collections import deque

moves = [(-1,0),(0,1),(1,0),(0,-1)]
N, M = map(int,input().rstrip().split())
r, c, direction = map(int,input().rstrip().split())

board = [list(map(int,input().rstrip().split())) for _ in range(N)]
visit = [[0]* M for _ in range(N)]

cnt = 0
def simulate(cur_x, cur_y, board, visit, direction, rotation_cnt):
    global cnt
        
    if board[cur_x][cur_y] != 7: #첫 방문 처리  
        board[cur_x][cur_y] = 7
        visit[cur_x][cur_y] = 1
        cnt +=1
    while rotation_cnt <=4 :
        new_direction = (direction-rotation_cnt)%4
        dx, dy =  moves[new_direction]
        next_x, next_y = cur_x + dx , cur_y + dy
        if next_x < 0 or next_y < 0 or next_x >=N or next_y >= M : 
            return simulate(cur_x, cur_y, board, visit, direction , rotation_cnt+1)
        if visit[next_x][next_y] or board[next_x][next_y] == 1 : 
            return simulate(cur_x, cur_y, board, visit, direction , rotation_cnt+1)
        visit[next_x][next_y] = 1
        board[next_x][next_y] = 7
        cnt+=1
        return simulate(next_x, next_y, board, visit, new_direction,1)
    
    if rotation_cnt == 5:
        dx, dy = moves[direction]
        next_x, next_y = cur_x -dx , cur_y - dy
        if board[next_x][next_y] == 1:
            return 
        return simulate(next_x, next_y, board, visit, direction,1)

simulate(r,c,board,visit,direction,1)
print(cnt)
    