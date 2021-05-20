#1766. 문제집
"""
위상정렬을 조건으로 하되, 난이도의 조건까지 신경써야 하는 문제.

edge의 순서는 위상정렬의 로직이 잘 구현해줄 것이므로, 

힙을 만들어서 이걸 구현하면 될 것 같다.

파이썬의 heapq는 min_heap이므로 난이도가 쉬운 문제부터 들어가겠지.
"""

#Step 1. Graph Setting
import sys
import heapq
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
    q=[]
    for node in range(1,N+1): 
        if indegree[node]==0: heapq.heappush(q,node)
    while q:
        cur_node=heapq.heappop(q)
        result.append(cur_node)
        for near_node in graph[cur_node]:
            indegree[near_node]-=1
            if indegree[near_node]==0: heapq.heappush(q,near_node)
    return result
                
res=topology_sort()
print(*res,end=" ")        
        
    
