from typing import List
from collections import defaultdict 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graphs = defaultdict(list)
        for start, end in prerequisites:
            graphs[start].append(end)
        
        traced = set() 
        visited = set()

        def dfs(cur_node):
            if cur_node in traced:
                return False 
            
            if cur_node in visited:
                return True

            traced.add(cur_node)
            
            for near_node in graphs[cur_node]:
                if not dfs(near_node):
                    return False

            traced.remove(cur_node)

            visited.add(cur_node)
            return True

        for node in list(graphs):
            if not dfs(node):
                return False 
        return True
        




            



        