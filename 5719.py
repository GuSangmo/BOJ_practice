# 

"""
최단 경로인지부터 세주자!
"""

import sys 
import heapq 
from collections import defaultdict , deque

input = sys.stdin.readline 

#0. Pre-setting

INF = float("inf")
def solve(N, M, start_city, end_city):
    #2. Dijkstra setting 
    costs = [INF] * (N+1)
    prevs = defaultdict(deque)

    def dijkstra(start, near_optimal = False, optimal_routes = None):
        q = []
        costs[start] = 0
        prevs[start] = []
        heapq.heappush(q,(0,start))

        while q: 
            cur_cost, cur_node = heapq.heappop(q)        
            if costs[cur_node] < cur_cost : continue

            for near_node, near_cost in graphs[cur_node]:
                
                #If near_optimal, ignore the result of optimal edges
                if near_optimal and optimal_routes[(cur_node, near_node)] > 0 : continue
                
                
                dist_candidate = cur_cost + near_cost 
                if costs[near_node] < dist_candidate: continue 

                # Duplicate, but can track multiple routes
                elif costs[near_node] == dist_candidate:
                    #여기만 바꾸면 충분!
                    prevs[near_node].append(cur_node)

                # Find minimum path
                else: 
                    prevs[near_node] = deque([cur_node])
                    costs[near_node] = dist_candidate 
                    heapq.heappush(q,(dist_candidate, near_node))

    #3. Define helper ftn to track min_path 

    def traceback_bfs(start):
        deq = deque([(start, [start])])
        results = []
        while deq:
            cur_node, cur_traverse = deq.popleft()
            if cur_node == start_city : 
                results.append(cur_traverse[::-1])
                continue
            for near_node in prevs[cur_node]:
                #If already visited , should ignore it 
                deq.append((near_node , cur_traverse+ [near_node]))
        return results
    
    #4. Get min_path
    dijkstra(start_city) 
    tracebacks = traceback_bfs(end_city)
    optimal_routes = defaultdict(int)
    for route in tracebacks:
        for idx in range(len(route)-1):
            optimal_routes[(route[idx], route[idx]+1)] = 1
        
    #5. Do near-optimal dijkstra
    costs = [INF] * (N+1)
    dijkstra(start_city, near_optimal = True, optimal_routes = optimal_routes)
    
    print(costs[end] if costs[end] < INF else -1)







#2. Input processing 


graphs = defaultdict(list)


stop_condition = True

while not stop_condition:
    N, M = map(int,input().rstrip().split())
    if N == 0 and M == 0 : break
    start_city, end_city = map(int,input().rstrip().split())
    for _ in range(M):
        start, end, cost = map(int,input().rstrip().split())
        graphs[start].append((end,cost))
    solve(N,M,start_city, end_city)
    

    
