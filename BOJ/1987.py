#1987. 알파벳
"""
그동안의 정보를 set에 저장시키자
"""

import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100_000)
R, C = map(int,input().rstrip().split())

boards = [list(input().rstrip()) for _ in range(R)]

for row in range(R):
    for col in range(C):
        boards[row][col] = ord(boards[row][col])-65

visits = [[False] * C for _ in range(R)]
maximum = 1
digits = [False for _ in range(26)]


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(distance, cur_x, cur_y, digits):
    global maximum 
    maximum = max(maximum, distance)
    if distance == 26: return 26
    for i in range(4):
        nx, ny = cur_x + dx[i] , cur_y + dy[i]
        if nx< 0 or ny<0 or nx>=R or ny>= C : continue
        if visits[nx][ny] or digits[boards[nx][ny]]: continue 
        digits[boards[nx][ny]] = True
        if distance == 25:
            digits[boards[nx][ny]] = False
            return 26
        dfs(distance+1, nx, ny, digits)
        digits[boards[nx][ny]] = False
    return maximum

digits[boards[0][0]] = True
answer = dfs(1, 0,0, digits)

print(answer)
