from typing import List
from collections import defaultdict 
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graphs = defaultdict(list)
        #Compose graph 
        for start,end, cost in times:
            graphs[start].append((end,cost))
        
        #Cost graphs
        INF = float("inf")
        costs = [INF] * (n+1)

        def dijkstra(start_node):
            q = []
            costs[start_node] = 0
            heapq.heappush(q, (0, start_node))

            while q:
                cur_cost, node = heapq.heappop(q)

                #Remove already visited
                if costs[node] < cur_cost : continue 

                for next_node, next_cost in graphs[node]:
                    print(f"from: {node} => To: {next_node}")
                    if costs[next_node] <= cur_cost + next_cost: continue 
                    costs[next_node] = cur_cost + next_cost 
                    heapq.heappush(q,(cur_cost + next_cost, next_node))
        
        #Execute
        dijkstra(k)

        maximum = -INF

        print("costs:", costs)
        for idx, time in enumerate(costs):
            if idx== 0 : continue
            maximum = max(time, maximum)
            if time == INF:
                return -1

        return maximum

s = Solution() 

times = [[1,2,1]]; n = 2; k = 2

s.networkDelayTime(times,n,k)