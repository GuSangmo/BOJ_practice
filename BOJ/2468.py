#2468. 안전영역
"""
DFS로 풀어보자

장마의 높이를 H라 한후, H미만은 다 0으로 padding한다.
그 후 영역의 개수를 센다.
"""

import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100_000)
N = int(input().rstrip())
boards = [list(map(int,input().rstrip().split())) for _ in range(N)]
max_height = max([max(row) for row in boards])


def dfs(start_x, start_y, height):
    global visits
    if visits[start_x][start_y] or boards[start_x][start_y] <= height:
        return False

    visits[start_x][start_y] = True
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = start_x + dx[i]
        ny = start_y + dy[i]
        if nx< 0 or ny<0 or nx>= N or ny>=N : continue 
        if boards[nx][ny] <= height : continue
        dfs(nx,ny,height)
    return True

answer = -1
for height in range(max_height+1):
    safe_zone = 0
    visits = [[False for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if dfs(row, col, height):
                safe_zone +=1
    answer = max(answer, safe_zone)
print(answer)
