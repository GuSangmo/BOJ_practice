#20183. 골목 대장 호석
"""
수치심 = max_path
max_path와 budget_sum을 모두 고려하면 충분하다.
"""

from collections import defaultdict 
import sys 
import heapq 
input = sys.stdin.readline

#1. Input processing 

N, M, start, end, budget = map(int,input().rstrip().split())
graphs = defaultdict(list)

for _ in range(M):
    U, V, C = map(int,input().rstrip().split())

    #Bi-direction
    graphs[U].append((V,C))
    graphs[V].append((U,C))

#2. Dijkstra setting

INF = float("inf")
costs = [INF] * (N+1)
visits = [False] * (N+1)
def dijkstra(start, total_budget):
    q =  []
    costs[start] = 0
    """
    heap has cost(embarrassment) / total_budget / node_number
    """
    heapq.heappush(q, (0,0,start))

    while q:
        cur_cost, budget, cur_node = heapq.heappop(q)
        #If already visited / No money available
        if costs[cur_node] <= cur_cost or total_budget < budget: continue 

        for near_node, near_cost in graphs[cur_node]:
            cost_candidate = max(cur_cost, near_cost)
            # If renewal possible despite budget, renewal it
            if cost_candidate < costs[near_node] and budget+ near_cost <= total_budget:
                costs[near_node] = cost_candidate
                heapq.heappush(q, (cost_candidate, budget+ near_cost, near_node))
dijkstra(start, budget)

print(costs[end] if costs[end]<INF else -1)        