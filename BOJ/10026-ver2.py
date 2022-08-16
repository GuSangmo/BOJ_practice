#10026. 적록색약
"""
DFS로 푸는건 처음이다.
"""
import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100_000)

N = int(input().rstrip())
pictures = [list(input().rstrip()) for _ in range(N)]

visit_original = [[False for _ in range(N)] for _ in range(N)]
visit_redgreen = [[False for _ in range(N)] for _ in range(N)]

def dfs(s_x, s_y, start_color):
    global visit_original
    visit_original[s_x][s_y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx , ny = s_x + dx[i], s_y +dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N : continue 
        if visit_original[nx][ny] : continue
        if pictures[nx][ny] != start_color : continue 
        visit_original[nx][ny] = True
        dfs(nx,ny, start_color)
    return True

def dfs_rg(s_x, s_y, start_color):
    global visit_redgreen
    visit_redgreen[s_x][s_y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx , ny = s_x + dx[i], s_y +dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N : continue 
        if visit_redgreen[nx][ny] : continue
        if pictures[nx][ny] != start_color : 
            if start_color == "B" or pictures[nx][ny] == "B": continue 
        visit_redgreen[nx][ny] = True
        dfs_rg(nx,ny, start_color)
    return True

original_zone_cnt = 0
redgreen_zone_cnt = 0
for i in range(N):
    for j in range(N):
        color = pictures[i][j]
        if not visit_original[i][j] :
            if dfs(i,j,color):
                original_zone_cnt +=1 
        if not visit_redgreen[i][j]:
            if dfs_rg(i,j,color):
                redgreen_zone_cnt +=1
print(original_zone_cnt, redgreen_zone_cnt)
