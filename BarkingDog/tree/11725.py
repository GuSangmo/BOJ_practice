#11725. 트리의 부모 찾기
import sys 
input = sys.stdin.readline
from collections import deque
N = int(input().rstrip())

parents = [0 for _ in range(N+1)]
graphs = [[] for _ in range(N+1)]

#Root 노드 고정
parents[1] = 1

for _ in range(N-1):
    node1, node2 = map(int,input().rstrip().split())
    graphs[node1].append(node2)
    graphs[node2].append(node1)


def bfs(start):
    deq = deque([start])
    while deq:
        cur_node = deq.popleft()
        for near_node in graphs[cur_node]:
            #Parent or Child
            if parents[cur_node] == near_node: 
                continue
            parents[near_node] = cur_node 
            deq.append(near_node)


#Execute!
bfs(1)

for node in range(2,N+1):
    print(parents[node])