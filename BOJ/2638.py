#2638. 치즈 
"""
2636번과 다른 것은, 인접한 2변 이상이 실내 공기와 접촉해야한다는 것!
따라서 녹을 치즈의 위치를 보관하는 자료구조만 변경하면 충분할 것 같다.
"""

import sys 
input = sys.stdin.readline 
from collections import deque, Counter

N,M = map(int,input().rstrip().split())

boards = []
visit = [[0] * M for _ in range(N)]


cheeze_count = 0
for row in range(N):
    rows = list(map(int,input().rstrip().split()))
    for col in range(M):
        if rows[col] == 1: 
            cheeze_count +=1
    boards.append(rows)

    
melt_time = 0
    
    
def bfs_melt(s_x, s_y, visit):
    """
    (0,0)에서 시작하여 bfs를 해가면서 다음에 녹을 애들을 melt_candiate에 담는 함수
    """
    global boards
    melt_cnt = 0
    visit[s_x][s_y] = 1 
    deq = deque([(s_x,s_y)])
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    melt_candidate = dict()
    while deq: 
        cur_x, cur_y = deq.popleft()        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i] 
            if nx<0 or ny<0 or nx>=N or ny>= M : continue 
            if visit[nx][ny] : continue     
            if boards[nx][ny] == 1:
                
                """
                원래는 visit을 0에 대해서 해야 하지만, 중복을 막기 위해.
                """
                
                melt_cnt = melt_candidate.get((nx,ny), 0)
                melt_candidate[(nx,ny)] = melt_cnt +1                
                continue 
            visit[nx][ny] = 1 
            deq.append((nx,ny))
    result = []             
    for melt_x, melt_y in melt_candidate: 
        if melt_candidate[(melt_x,melt_y)] >=2:
            boards[melt_x][melt_y] -= 1 
            result.append((melt_x,melt_y))
    return result
            
while cheeze_count>0: 
    melt_time +=1
    visit = [[0] * M for _ in range(N)]
    result = bfs_melt(0,0, visit)
    # print(f">>>>>> time {melt_time} : {len(result)} should melt || Remainder : {cheeze_count - len(result)}")
    cheeze_count -= len(result)
    
    
    # for row in boards: print(row, sep = "\n")
    

print(melt_time)

