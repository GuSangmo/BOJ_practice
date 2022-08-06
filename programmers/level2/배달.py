"""
Progarmmers Lv2. 

다익스트라
"""

"""
8 Min
Common dijkstra
"""


import heapq 
from collections import defaultdict

def solution(N, road, K):
    answer = 0
    graphs = defaultdict(list)
    for start, end, cost in road:
        graphs[start].append((end,cost))
        graphs[end].append((start,cost))
    
    INF = float("inf")
    
    def dijkstra(start):
        costs = [INF for _ in range(N+1)]
        costs[start] = 0
        q = []
        heapq.heappush(q,(0,start))
        while q: 
            cur_cost, cur_node = heapq.heappop(q)
            
            #If already modified, then pass
            if costs[cur_node] < cur_cost : continue 
            
            for near_node, near_cost in graphs[cur_node]:
                if cur_cost + near_cost < costs[near_node]:
                    graphs[cur_node] = cur_cost + near_cost 
                    costs[near_node] = cur_cost + near_cost 
                    heapq.heappush( q, (cur_cost+near_cost, near_node))
        return costs 
    costs = dijkstra(1)
    answer = sum([1 for idx in range(1,N+1) if costs[idx] <=K])

    return answer