#1238. 파티
"""
N=1000, M=10000이므로 

M log N이 보장된 다익스트라를 N번 시도해보자.

NM log N= 1억... 

아슬아슬할것 같은데 한번 해보자.
"""

import sys
import heapq
input=sys.stdin.readline
N,M,X=map(int,input().rstrip().split())
big_num= 1e8



graph=[[] for _ in range(N+1)]
dist=[big_num]*(N+1)

for _ in range(M):
    start,end,length=map(int,input().rstrip().split())
    graph[start].append((end,length))

#DIJKSTRA

def dijkstra(start,origin_dist):
    dist=origin_dist[:]
    q=[]
    dist[start]=0
    heapq.heappush(q,(0,start))
    while q:
        cur_dist, cur_node= heapq.heappop(q)
        if dist[cur_node]<cur_dist: continue
        for near_node, near_dist in graph[cur_node]:
            candidate=dist[cur_node]+near_dist
            if dist[near_node]>candidate:
                dist[near_node]=candidate
                heapq.heappush(q,(candidate,near_node))
    return dist

maximum=-2e9

comeback=dijkstra(X,dist) #X에서 출발한 것

for start in range(1,N+1):
    res=dijkstra(start,dist)
    time=comeback[start]+res[X]
    maximum=max(time,maximum)
print(maximum)
        
        
        
        
    

    
    
    
    
    