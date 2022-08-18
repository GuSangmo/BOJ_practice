#11048. 이동하기
from collections import deque 
import sys 
input = sys.stdin.readline 
N, M = map(int,input().rstrip().split())
candies = [list(map(int, input().rstrip().split())) for _ in range(N)]
results = [[0 for _ in range(M)] for _ in range(N)]
visits = [[False for _ in range(M)] for _ in range(N)]

print("candies:", *candies, sep = "\n")
def bfs(s_x, s_y):
    global visits
    dx = [1,0]
    dy = [0,1]
    results[s_x][s_y] = candies[s_x][s_y]
    deq = deque([(s_x,s_y)])
    while deq:
        cur_x, cur_y = deq.popleft()
        for i in range(2):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>= M : continue 
            results[nx][ny] = max(results[nx][ny], candies[nx][ny] +results[cur_x][cur_y])
            if visits[nx][ny]:
                continue
            visits[nx][ny] = True 
            deq.append((nx,ny))

bfs(0,0)

print("resul;ts:", *results, sep = "\n")
print(results[N-1][M-1])