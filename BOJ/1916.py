#1916. 최소비용 구하기
"Now, Implement Dijkstra Algorithm yourself, without hints by others"



#Step 1. INITIAL SETTING
import sys
import heapq

input=sys.stdin.readline
N=int(input().rstrip())
M=int(input().rstrip())
#총 1000개의 도시, 비용은 최대 10만이므로, big_num은 2e8로 표시.
big_num=2e8

graph=[[] for _ in range(N+1)] #Zero padding for efficient idx
dist=[2e8]*(N+1) #주어진 시작점에서 각 node까지 가기 위한 거리의 최소값


for _ in range(M):
    start,end,cost=map(int,input().rstrip().split())
    graph[start].append((end,cost))

#Step 2. Dijkstra Execution

def dijk(start):
    dist[start]=0
    deq=[]
    heapq.heappush(deq,(0,start))
    while deq:
        cur_dist, cur_node=heapq.heappop(deq)
        if dist[cur_node]<cur_dist: continue #얜 쓸모없지 그러면 
        for near_node, cur_to_near_cost in graph[cur_node]:
            dist_tmp=cur_dist+cur_to_near_cost #cur_node를 거쳐서 가는 경우의 거리
            if dist_tmp<dist[near_node]: 
                dist[near_node]=dist_tmp #더 효과적이니까 갱신해주고,
                heapq.heappush(deq,(dist_tmp,near_node))
            
start_node, end_node= map(int,input().rstrip().split())

dijk(start_node)
print(dist[end_node])







