#11780. 플로이드 2
"""
이번엔 플로이드 워셜의 실제 최단 경로를 구하는 문제.

prev 배열을 선언하자.


prev배열보단 recursive하게 하는게 낫다. 이유는 


i->k->j 를 구하는 과정에서 k->j 까지 계속 출력해야 하기 때문이다.


"""

#Step 1. INITIALIZATION
import sys
input=sys.stdin.readline
N=int(input().rstrip())
M=int(input().rstrip())
big_num= int(1e8)
graph=[[big_num]*(N+1) for _ in range(N+1)]
dist=[[big_num]*(N+1) for _ in range(N+1)]
prev=[[-1]*(N+1) for start in range(N+1)]
for _ in range(M):
    start,end,cost=map(int,input().rstrip().split())
    graph[start][end]=min(graph[start][end],cost)

#Distance matrix Setting
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j: dist[i][j]=0
        elif 0<graph[i][j]<big_num: dist[i][j]=graph[i][j]
            
#Step 2. Floyd-warshall
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dist[i][k]+dist[k][j]<dist[i][j]:
                dist[i][j]=dist[i][k]+dist[k][j]
                prev[i][j]=k #i에서 시작할때, j의 중간점을 갱신

## 최단 경로를 출력하기 위해, i->k+ k->j 를 각각 구해줘야하므로 recursive하게 구현.

def get_path(i,j):
    if prev[i][j]==-1: return []
    else:
        k=prev[i][j]
        return get_path(i,k)+[k]+get_path(k,j)

#Step 3. Result Execution
"""
각 node에서 node 까지의 거리들 출력
"""

for i in range(1,N+1):
    for j in range(1,N+1):
        print(dist[i][j] if dist[i][j]<big_num else 0,end=" ")
    print()

"""
실제 최단경로를 출력

"""    
for i in range(1,N+1):
    for j in range(1,N+1): #prev[i][j]:i가 시작점일때 i->j에서 최단경로중 j 직전에 방문한 노드
        if dist[i][j]==big_num or i==j: 
            print(0)
        else: #prev 배열을 반복적으로 찾아가며 시작점이 i가 될때까지 출력
            visits=[i]+get_path(i,j)+[j]
            print(len(visits),end=" ")
            print(*visits,end=" ")
            print()
        
        
        
        
    