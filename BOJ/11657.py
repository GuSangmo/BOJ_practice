#11657. 타임머신
"""
비용이 음수가 될 수 있으므로
벨만 포드 알고리즘을 이용한다.

N=500, M=6000이므로 NM=300만이라 충분할 것.
"""

import sys
input=sys.stdin.readline

N,M=map(int,input().rstrip().split())
big_num= 1e7

graph=[[] for _ in range(N+1)]
dist=[big_num]*(N+1)

#Adj_list 식으로 선언했음
for _ in range(M):
    start,end,time=map(int,input().rstrip().split())
    graph[start].append((end,time))

def bell_ford(start):
    negCycle=False
    dist[start]=0
    for term in range(N):
        for j in range(1,N+1):
            for near_node, near_cost in graph[j]:
                if dist[j]!=big_num and dist[near_node]>dist[j]+near_cost:
                    dist[near_node]=dist[j]+near_cost
                    if term==(N-1):
                        return True             
    return False

timeMachine=bell_ford(1)
if timeMachine:print(-1)
else:
    for i in range(2,N+1): print(dist[i] if dist[i]<big_num else -1)
        


