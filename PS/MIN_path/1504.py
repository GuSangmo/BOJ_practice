#1504. 특정한 최단 경로
"""
start->A, A->B, B->end
를 각각 구하면 된다.

N=800, E=20000이므로 
O(E log V)인 다익스트라를 쓰는 것이 좋다.

최대 거리는 20만 * 800 =1.6억이므로 INF=1e11선언.


1->a->b->N, 1->b->a->N 이 경우를 모두 고려해줘야 한다.

"""
import sys
import heapq
input=sys.stdin.readline
big_num=int(1e11)

N,E=map(int,input().rstrip().split())
graph=[[] for _ in range(N+1)] #Zero index
dist=[big_num]*(N+1)


for _ in range(E):
    start,end,cost=map(int,input().rstrip().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

    
def dijkstra(start,dist):
    dist=dist[:] #여러번 쓸 것이므로 그냥 복사했음
    dist[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cur_dist, cur_node= heapq.heappop(q) #거리가 최소인 걸 뽑아서
        if dist[cur_node]<cur_dist: continue #이미 갱신된 것.
        for near_node, near_distance in graph[cur_node]:
            candidate= dist[cur_node]+near_distance #cur_node를 통해 갱신될 수 있는가?
            if dist[near_node]>candidate:
                dist[near_node]=candidate
                heapq.heappush(q,(candidate,near_node))
    return dist

# Result Execution: 다익스트라를 3번 수행.
a,b=map(int,input().rstrip().split())

dist1= dijkstra(1,dist)
dist2= dijkstra(a,dist)
dist3= dijkstra(b,dist)

dist_sum=min(dist1[a]+dist2[b]+dist3[N], dist1[b]+dist3[a]+dist2[N])

print(dist_sum if dist_sum<big_num else -1)
