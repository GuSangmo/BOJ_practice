############################
# Level 3. 가장 먼 노드   ##
############################

# Time : 30 min

"""
Max_dist의 개수를 구하면 되므로, dists 배열 구한 후 갱신!
"""

from collections import defaultdict , deque
def solution(n, edge):
    graphs = defaultdict(list)
    dists = [-1 for _ in range(n+1)]
    for point1, point2 in edge:
        graphs[point1].append(point2)
        graphs[point2].append(point1)
        
    def bfs(start, dists):
        maximum_dist = -1
        deq = deque([start])
        dists[start] = 1
        while deq: 
            cur_node = deq.popleft()
            for near_node in graphs[cur_node]:
                #alreay visited 
                if dists[near_node] >=0 : continue 
                dists[near_node] = dists[cur_node]+1 
                maximum_dist = max(dists[near_node], maximum_dist)
                deq.append(near_node)
                
        summation = sum([1 for i in range(1,n+1) if dists[i] == maximum_dist])
        
        return summation
    #Exectute
    answer = bfs(1, dists)
    
    return answer
   
                           
                           
    
    
