#1240. 노드 사이의 거리
"""
root 로부터의 거리를 보면 충분할 것 같은데
몇번 거슬러 올라가야하냐로 따질 수 있을것같아

처음에 traverse 하며 depth를 갱신하고, 

쿼리를 받은 뒤엔 depth 가 같아질 때까지 한 놈을 갱신한 후
같은 노드면 break하고, 아니면 parent가 같을때까지 해야지 뭐.
depth를 기준으로 받아야 하나.
"""


def get_node_dist(node1, node2, parents, depths, costs):
    depth1 = depths[node1]
    depth2 = depths[node2]
    dist = 0

    if depth1 < depth2:
        while depth2 != depth1:
            depth2 -= 1 
            dist += costs[parents[node2]][node2]
            node2 = parents[node2]
    elif depth1 > depth2:
        while depth2 != depth1:
            depth1 -= 1 
            dist += costs[parents[node1]][node1]
            node1 = parents[node1]

    while node1 != node2:
        #이미 같다면
        dist += costs[parents[node1]][node1] + costs[parents[node2]][node2]
        node1 = parents[node1]
        node2 = parents[node2]
    return dist


import sys 
input = sys.stdin.readline 
from collections import deque

N, M = map(int,input().rstrip().split())
graphs = [[] for _ in range(N+1)]
parents = list(range(N+1))
depths = [0 for _ in range(N+1)]
costs = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N-1):
    start, end, cost = map(int,input().rstrip().split())
    graphs[start].append(end)
    graphs[end].append(start)
    costs[start][end] = cost
    costs[end][start] = cost


def tree_traverse(node):
    deq =deque([(node,0)])
    while deq:
        cur_node, cur_depth = deq.popleft()
        for near_node in graphs[cur_node]:
            if parents[cur_node] == near_node:
                continue 
            parents[near_node] = cur_node
            depths[near_node] = cur_depth+ 1
            deq.append((near_node, cur_depth+1))

#Execute
tree_traverse(1)

#Query 


for _ in range(M):
    node1, node2 = map(int,input().rstrip().split())
    print(get_node_dist(node1, node2, parents, depths, costs))

