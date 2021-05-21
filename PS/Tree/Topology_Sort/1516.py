#1516. 게임 개발
"""
Type of Topology_Sort.
results를 초기화해놓고
indegree=0인 애들 넣을 때 cost를 초기화해야함.
간믈 v의 가장 빠른 완료시간은, 선행노드들+건축시간 중 제일 늦은거

"""

import sys
from collections import deque
input=sys.stdin.readline

N=int(input().rstrip())
graph=[[] for _ in range(N+1)]
indegree=[0]*(N+1)
costs=[-1]*(N+1)
for origin in range(1,N+1):
    cost,*others=map(int,input().rstrip().split())
    costs[origin]=cost
    if len(others)!=1: 
        others.pop()
        for prev in others:
            graph[prev].append(origin)
            indegree[origin]+=1
def topology_sort():
    q=deque()
    results=[0]*(N+1)
    for i in range(1,N+1):
        if indegree[i]==0:
            results[i]=costs[i]
            q.append(i)
    while q:
        cur_node=q.popleft()
        for near_node in graph[cur_node]:
            indegree[near_node]-=1
            results[near_node]=max(results[near_node],results[cur_node]+costs[near_node])
            if indegree[near_node]==0: q.append(near_node)
    return results  
                
result=topology_sort()
for i in range(1,N+1):print(result[i])