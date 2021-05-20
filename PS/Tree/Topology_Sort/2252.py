#2252. 줄 세우기
"""
위상정렬을 연습해보는 문제.

이번엔 한번 레퍼런스 없이 직접 해보자.

위상정렬의 원리는, indegree 배열을 만들어서 
bfs 느낌으로 하는 것. 

indegree=0인 애들을 먼저 넣은후, 인접한 node들의 indegree를 감소시키며 진행.
"""


#Step 1. Graph Setting
import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
graph=[[] for _ in range(N+1)]
indegree=[0]*(N+1)

for _ in range(M):
    front, end= map(int,input().rstrip().split())
    graph[front].append(end)
    indegree[end]+=1

#Step 2. Topology sort Definition
def topology_sort():
    result=[]
    q=deque([])
    for node in range(1,N+1): 
        if indegree[node]==0: q.append(node)
    while q:
        cur_node=q.popleft()
        result.append(cur_node)
        for near_node in graph[cur_node]:
            indegree[near_node]-=1
            if indegree[near_node]==0: q.append(near_node)
    return result
                
res=topology_sort()
print(*res,end=" ")        
        
    
