# 1162. 도로포장

"""
K를 count
"""

import sys 
import heapq 
from collections import defaultdict , deque

input = sys.stdin.readline 

#1. INPUT SETTING
INF = float("inf")

N, M, K = map(int,input().rstrip().split())



graphs = defaultdict(list)

for _ in range(M):
    start, end, cost = map(int,input().rstrip().split())
    graphs[start].append((end, cost))
    graphs[end].append((start,cost))

#cost of wrap or not
costs = [[INF for _ in range(K+1)] for _ in range(N+1)]
#start is always 0

for i in range(K+1):
    costs[1][i] = 0
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,0, start))

    while q: 

        cur_cost, cur_wrap ,cur_node = heapq.heappop(q)    
        if costs[cur_node][cur_wrap] < cur_cost or cur_wrap > K : continue
        for near_node, near_cost in graphs[cur_node]:

            #Just wrap and pass
            if cur_wrap <K:
                if costs[near_node][cur_wrap+1] > cur_cost:
                    costs[near_node][cur_wrap +1] = cur_cost
                    heapq.heappush(q,(cur_cost, cur_wrap+1, near_node))

            #If don't wrap
            cost_candidate = cur_cost + near_cost 
            if costs[near_node][cur_wrap] > cost_candidate:
                costs[near_node][cur_wrap] = cost_candidate 
                heapq.heappush(q,(cost_candidate, cur_wrap, near_node))

dijkstra(1) 

print(min(costs[N]))



    
    

    
