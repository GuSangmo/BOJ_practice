#11779. 최소비용 구하기 2
"""
경로복원을 시도해보자.

최단 거리의 역추적은 갱신되는 순간에 prev 배열을 만들어서 선언한다.

"""
import sys
import heapq
input=sys.stdin.readline
big_num=int(1e11)

N=int(input().rstrip())
M=int(input().rstrip())
graph=[[] for _ in range(N+1)] #Zero index
dist=[big_num]*(N+1)
prev=[-1]*(N+1)

for _ in range(M):
    start,end,cost=map(int,input().rstrip().split())
    graph[start].append((end,cost))

def dijkstra(start):
    dist[start]=0
    prev[start]=start
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cur_dist, cur_node= heapq.heappop(q) #거리가 최소인 걸 뽑아서
        if dist[cur_node]<cur_dist: continue #이미 갱신된 것.
        for near_node, near_distance in graph[cur_node]:
            candidate= dist[cur_node]+near_distance #cur_node를 통해 갱신될 수 있는가?
            if dist[near_node]>candidate:
                dist[near_node]=candidate
                prev[near_node]=cur_node                
                heapq.heappush(q,(candidate,near_node))
    return dist

# Result Execution: 최소 비용과 도시의 개수, 도시의 경로
A,B=map(int,input().rstrip().split())
result= dijkstra(A)
min_cost=result[B]



#Traceback
routes=[]
cur_node=B
while cur_node!=A:
    routes.append(cur_node)
    cur_node=prev[cur_node]
    if cur_node==A: routes.append(A);break
print(min_cost)
print(len(routes))
print(*routes[::-1],sep=" ")


