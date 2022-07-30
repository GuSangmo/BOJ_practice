# 11779_ver2.py

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
    costs = [INF] * N
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
                if near_optimal and optimal_routes[cur_node][near_node] : continue
                
                
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
    optimal_routes = [[False for _ in range(N)] for _ in range(N)]
    def traceback_bfs(end, costs):
        deq = deque([end])
        results = []
        while deq:
            cur_node  = deq.popleft()
            if cur_node == start_city : 
                continue
            for prev_node, prev_dist in graphs_reverse[cur_node]:
                if costs[prev_node] +  prev_dist == costs[cur_node] and not optimal_routes[prev_node][cur_node]:
                    deq.append(prev_node)
                    optimal_routes[prev_node][cur_node] = True

    
    #4. Get min_path
    dijkstra(start_city) 
    
    traceback_bfs(end_city, costs)
    
    #print("first dijkstra done")
    #print("first costs:", costs)

    #5. Do near-optimal dijkstra
    costs = [INF] * N
    dijkstra(start_city, near_optimal = True, optimal_routes = optimal_routes)
    
    #print("second dijkstra done")
    #print("second costs:", costs)
    print(costs[end_city] if costs[end_city] < INF else -1)


#2. Input processing 

stop_condition = False

while not stop_condition:
    graphs = defaultdict(list)
    graphs_reverse = defaultdict(list)
    N, M = map(int,input().rstrip().split())
    if N == 0 and M == 0 : break
    start_city, end_city = map(int,input().rstrip().split())
    for _ in range(M):
        start, end, cost = map(int,input().rstrip().split())
        graphs[start].append((end,cost))
        graphs_reverse[end].append((start,cost))
    solve(N,M,start_city, end_city)
    
    

    
