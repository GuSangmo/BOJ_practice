#1005. ACM CRAFT
"""
마찬가지로 최대 시간을 구하는 문제.
parent node들로부터의 누적 갱신 시간을 비교해서 최대값으로 갱신시켜주면 충분하다.

10 minute
"""

import sys 
from collections import deque 
input = sys.stdin.readline 

T = int(input().rstrip())
for _ in range(T):
    N, K = map(int,input().rstrip().split())
    times = [0] + list(map(int,input().rstrip().split()))
    graphs = [[] for _ in range(N+1)]
    indegrees = [0 for _ in range(N+1)]
    cumuls = [0 for _ in range(N+1)]

    #I/O 처리, 그래프 처리
    for i in range(K):
        prev, after = map(int,input().rstrip().split())
        graphs[prev].append(after)
        indegrees[after] +=1 
    
    # Topology sort 시작을 위한 deq선언 
    deq = deque([])
    for node in range(1,N+1):
        if indegrees[node] == 0 :
            deq.append(node)
            cumuls[node] = times[node]

    # Topology_sort 
    while deq:
        cur_node = deq.popleft()
        for near_node in graphs[cur_node]:
            indegrees[near_node] -=1 
            #시간 갱신 
            cumuls[near_node] = max(cumuls[near_node], cumuls[cur_node] + times[near_node])
            if indegrees[near_node] == 0 :
                deq.append(near_node)
    
    #Special building
    special_building = int(input().rstrip())
    print(cumuls[special_building])


    


