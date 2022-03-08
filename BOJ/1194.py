#1194. 달이 차오른다, 가자!
"""
Bitmasking + BFS Technique 

상태공간의 정의 

dists[i][j][key] = (i,j)인데 현재 status가 key인 것.
"""

import sys 
input = sys.stdin.readline 
from collections import deque 

N,M = map(int, input().rstrip().split())

boards = []
start = (-1,-1)
ends = []

dists = [[[-1] * M for _ in range(N)] for _ in range(64)]

for row in range(N):
    each_row = list(input().rstrip())
    boards.append(each_row)
    for col in range(M):
        if each_row[col] == "0" :  
            start = (row,col)
        elif each_row[col] == "1" :
            ends.append((row,col))

            
            
#방문 로직은 bfs 함수에서 검증하자!
"""
2500 * 64


- RangeOut / Visit 여부 확인

- Key가 있을 때 방문가능 여부 확인! (status check)

"""

s_row, s_col = start

dists[0][s_row][s_col] = 0
deq = deque([(0,s_row,s_col)])

dx = [-1,1,0,0]
dy = [0,0,1,-1]




def bfs(deq, dist):
    while deq:
        key, cur_x, cur_y = deq.popleft()
        # print(f"key:{key}, cur_x:{cur_x}, cur_y:{cur_y}, distance: {dists[key][cur_x][cur_y]}")
        for i in range(4):
            nx = cur_x + dx[i] ; ny = cur_y + dy[i]
            #Rangeout, Visit, Wall 무시
            if nx<0 or ny<0 or nx>=N or ny>=M : continue 
            if boards[nx][ny] == "#" : continue
            if dists[key][nx][ny]>=0: 
                continue
                
            if boards[nx][ny].islower():
                order = ord(boards[nx][ny])-97
                new_key = (key | (1<<order))
                dists[new_key][nx][ny] = dists[key][cur_x][cur_y]+1
                deq.append((new_key, nx, ny))
            elif boards[nx][ny].isupper():
                order = ord(boards[nx][ny])-65 
                if (key & (1<<order)) : 
                    dists[key][nx][ny] = dists[key][cur_x][cur_y]+1
                    deq.append((key, nx,ny))
                else: continue # 방문 못함 
            else:
                dists[key][nx][ny] = dists[key][cur_x][cur_y]+1
                deq.append((key,nx,ny))
                
                    
    result = 1e10
    for end_row, end_col in ends:
        for status in range(64):
            if dists[status][end_row][end_col] == -1 : continue 
            result = min(result, dists[status][end_row][end_col])
    
    if result ==1e10: return -1
    elif result<1e10: 
        return result 
    
ans = bfs(deq, dists)


#if N==1 and M==1:
#   if boards[0][0] == "1": ans = 1 
#  elif boards[0][0] == "0": ans = -1
            
print(ans)
            
        
        
    
    



