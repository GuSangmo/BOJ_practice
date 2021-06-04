#11724. 연결 요소의 개수

"""
연결 요소의 개수: 

[1] BFS
-> 그래프를 만든 후 하나씩 세기

[2] 위상정렬
-> 다 union-find를 적용시킨 후 set으로 parent(i) 뽑기.

등의 2가지 정도가 떠오른다.

뭘 하든 시간은 충분할듯.
"""



##Setting
import sys
import collections
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())

graph=[[] for _ in range(N+1)]
for _ in range(M):
    start,end=map(int,input().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

    
##BFS    
visit_graph=[0] *(N+1)
connected=0
def bfs(start,visit, graph):
    deq=collections.deque([])
    deq.append(start)
    visit[start]=1
    while deq:
        curr=deq.popleft()
        for near_node in graph[curr]:
            if visit[near_node]: continue
            visit[near_node]=1
            deq.append(near_node)
##연결 요소의 개수 세기
for node in range(1,N+1):
    if visit_graph[node]==0:
        bfs(node,visit_graph,graph)
        connected+=1
print(connected)








