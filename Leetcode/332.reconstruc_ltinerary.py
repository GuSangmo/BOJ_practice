from typing import List
from collections import defaultdict, deque
from copy import deepcopy

# 6: 10 ~ 
class Solution:

    def constructGraph(self, tickets):
        graphs = defaultdict(list)
        node_cnt = 0
        for from_node, to_node in sorted(tickets):
            graphs[from_node].append(to_node)
            node_cnt +=1
        return graphs, node_cnt


    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph, total_node = self.constructGraph(tickets)
        def dfs_ticket(start, route, node_cnt):
            if node_cnt == total_node : return route

            for idx, near_node in  enumerate(graph[start]):
                print("near_node:", near_node, "from:", start)
                graph[start].remove(near_node)
                dfs_ticket(near_node, route + [near_node], node_cnt+1)
                graph[start].insert(idx, near_node)

        #Execute!!!
        routes = dfs_ticket("JFK", ["JFK"],0)

        return routes

s = Solution()

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

print(s.findItinerary(tickets))