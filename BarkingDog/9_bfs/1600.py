#1600. 말이 되고픈 원숭이
"""
말 방식으로 이동하는 것도 표시하되, 이 경우 
한 층 뚫고 가게 하기!
"""

import sys
input = sys.stdin.readline
from collections import deque


#1. I/O 처리
K = int(input().rstrip())
W, H = map(int,input().rstrip().split() ) # 순서 조심
board = [list(map(int,input().rstrip().split())) for _ in range(H)]
dist  = [[[-1]* W for _ in range(H)] for _ in range(K+1)] #dist배열 선언
dist[0][0][0] = 0
#index 순서 : K - H - W



#2. BFS logic 
"""
일반적인 이동은 그냥 그대로 처리하되, 
말을 흉내낼 때는 1층씩 아래로 내려가게 하자.
"""

def bfs(x,y,drill, dist, H, W):
    
    if H==1 and W==1 : return 0
    
    deq = deque([(drill,x,y)])
    #일반적인 경로 흉내
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    #말의 경로 흉내
    hx = [1,1,-1,-1,2,2,-2,-2]
    hy = [2,-2,2,-2,1,-1,1,-1]
    cur_height = 0
    
    
    results = []
    
    while deq:
        horse, cur_x, cur_y = deq.popleft()
        if cur_x == H-1 and cur_y == W-1 : results.append(dist[horse][H-1][W-1])
        # print("cur_x, cur_y, cur_height:", cur_x, cur_y, horse)
        #헷갈리지 않도록 하기 위해 일반적인 이동과 말의 이동을 다른 for문에 놓자.
        for i in range(4):
            nx = cur_x+dx[i]; ny = cur_y+dy[i]
            if nx<0 or ny<0 or nx>=H or ny>=W : continue  
            if dist[horse][nx][ny]>=0 or board[nx][ny] == 1: continue
            dist[horse][nx][ny] = dist[horse][cur_x][cur_y] +1
            deq.append((horse,nx,ny))

        for i in range(8): 
            mx = cur_x+hx[i]; my = cur_y+ hy[i]
            if mx<0 or my<0 or mx>=H or my>=W : continue
            if board[mx][my] == 1: continue
            
            #말은 쓸때마다 한 칸씩 뚫는거랑 비슷하다.
            if horse == K: continue            
            if dist[horse+1][mx][my] >=0 : continue
            dist[horse+1][mx][my] = dist[horse][cur_x][cur_y]+1 #min을 쓰면 안된다.
            deq.append((horse+1,mx,my))            
            
    
    #results에는 -1과 -1이 아닌 값들이 담겨있음
    nonnegatives = [] ; flag = False
    for value in results:
        if value!= -1:
            nonnegatives.append(value)
            flag = True
    return min(nonnegatives) if flag else -1
        
answer = bfs(0,0,0,dist,H,W)

print(answer)
