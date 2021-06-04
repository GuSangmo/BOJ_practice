#18405. 경쟁적 전염
"""
heapq를 쓰는법도 있을것만 같지만 일단 이렇게 구현했다.
"""
#STEP 1. INPUT SETTING
import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().rstrip().split())
board=[]
dist=[[-1]* N for _ in range(N)]
start_deq=deque([])
for row in range(N):
    arr=list(map(int,input().rstrip().split()))
    board.append(arr)
    for col in range(N):
        if arr[col]: 
            dist[row][col]=0 #바이러스가 들어있는건 거리 0으로 설정.
            start_deq.append((row,col))

#STEP 2. OPERATION START(BFS, ON)

def bfs(deq, board, dist):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    #이미 시작점은 넣어놨으니 start부분 작업할 필요 없음
    while deq:
        x,y=deq.popleft()
        
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N: continue
            if dist[nx][ny]>=0: #이미 방문한 적이 있는데, 하필 나랑 같은 우선순위라면
                if dist[nx][ny]==dist[x][y]+1:                
                    board[nx][ny]=min(board[nx][ny],board[x][y]) #더 빠른놈이 먹겠지
                continue
            board[nx][ny]=board[x][y]
            dist[nx][ny]=dist[x][y]+1
            deq.append((nx,ny))
bfs(start_deq,board,dist)


# #바이러스 확인용
# print("-------board--------")
# for row in board: 
#     print(row)

    
# print("-------dist---------")
# for row in dist:
#     print(row)
    
#결과 출력용
S,X,Y=map(int,input().rstrip().split())
result= int(dist[X-1][Y-1]<=S) * board[X-1][Y-1] 
print(result)
                
            
            
            
        
        
        
        
        
        
    
    
    
    







