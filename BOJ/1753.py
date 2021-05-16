#1753. 최단 경로
"""
Use: Dijkstra's Algorithm

E=300,000이므로 다익스트라 알고리즘을 쓰는게 효과적.

V=20,000이므로 V^2에 달하는 mtx를 만들기엔 메모리 초과가 생긴다.

따라서 인접리스트를 이용한 heapq를 만들어 풀자.

이때 중복처리를 위해 dict로 선언해주자.

big_num때문에 틀렸다. 최대 10* 30만= 300만까지 들어올 수 있는 것이었는데. 1e7을 선언하는게 맞는듯.

"""

import sys
import heapq


input=sys.stdin.readline
V,E=map(int,input().rstrip().split())
big_num=int(1e7)
#인접리스트, 거리리스트 선언 선언
start_node=int(input().rstrip())
graph=[[] for i in range(V+1)]
dist=[big_num]*(V+1) #시작점에서 주어진 node까지의 최단거리를 담은 테이블


for _ in range(E):
    start,end,cost=map(int,input().rstrip().split())
    graph[start].append((end,cost))

#다익스트라 함수 구현
def dijk(start):
    dist[start]=0
    deq=[]
    heapq.heappush(deq,(0,start))
    while deq:
        cur_dist, cur_node= heapq.heappop(deq)
        if dist[cur_node]< cur_dist: continue #최단거리가 될 가능성이 없으면 입구컷
        for near_node, near_cost in graph[cur_node]: #인접한 노드들 중에서 최단거리보다 짧을 가능성이 있는지 check      
            dist_candidate=cur_dist+near_cost
            if dist_candidate<dist[near_node]: #이거 notation을 잘못했음.
                heapq.heappush(deq,(dist_candidate,near_node)) #최단거리가 업데이트된 것!
                dist[near_node]=dist_candidate
dijk(start_node)

for i in range(1,V+1):
    print(dist[i] if dist[i]<big_num else "INF")






















