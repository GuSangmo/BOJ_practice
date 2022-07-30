#17835. 면접보는 승범이네
"""
면접장들을 공통된 시작점 큐에 넣으면, 인접한 곳들을 모두 비슷하게 판별할 것!

면접장을 시작점으로 넣으므로, 그래프를 반대로 입력받자!

그 면접장들에서 가장 먼 곳을 출력하면 충분하다.

"""

from collections import defaultdict 
import sys 
import heapq 
input = sys.stdin.readline

#1. Input processing 

N, M, K = map(int,input().rstrip().split())
graphs = defaultdict(list)
test_dict = defaultdict(int)

for _ in range(M):
    U, V, C = map(int,input().rstrip().split())
    graphs[V].append((U,C))

test_points = list(map(int,input().rstrip().split()))
#2. Dijkstra setting
INF = 1e11
costs = [INF] * (N+1)
def dijkstra(start_points):
    q =  []
    for start_point in start_points:
        costs[start_point] = 0
        # push cost and node
        heapq.heappush(q, (0,start_point))

    while q:
        cur_cost, cur_node = heapq.heappop(q)
        #If already visited, continue
        if costs[cur_node] < cur_cost : continue 

        for near_node, near_cost in graphs[cur_node]:
            cost_candidate = cur_cost + near_cost
            # If renewal possible, renewal it
            if cost_candidate < costs[near_node]:
                costs[near_node] = cost_candidate
                heapq.heappush(q, (cost_candidate, near_node))
dijkstra(test_points)

max_idx = -1 ; max_dist = -1
for idx, cost in enumerate(costs):
    if idx == 0 : continue 
    if cost > max_dist:
        max_dist = cost 
        max_idx = idx 
print(max_idx)
print(max_dist)
        