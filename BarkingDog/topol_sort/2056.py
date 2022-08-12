#2056. 작업
"""
시간을 구하는 문제인데, 마지막 leaf node의 max_time을 구하면 되지 않을까.
이때, 이전 선행 작업들이 다 끝나야 time이 진행될 수 있기에 near_node는 계속 max값으로 유지시켜주자.

"""

import sys 
from collections import deque 
input = sys.stdin.readline 


N = int(input().rstrip())
graphs = [[] for _ in range(N+1)]
indegrees = [0 for _ in range(N+1)]
times = [0 for _ in range(N+1)]
cumuls = [0 for _ in range(N+1)]
#I/O 처리, 그래프 처리
for i in range(1,N+1):
    time, _, *sequential = map(int,input().rstrip().split())
    times[i] = time
    for sequence in sequential:
        graphs[sequence].append(i)
        indegrees[i] +=1

#Graph처리 
deq = deque([])
for node in range(1,N+1):
    if indegrees[node] == 0 :
        deq.append(node)
        cumuls[node] = times[node]

max_time = -1
while deq:
    cur_node = deq.popleft()
    for near_node in graphs[cur_node]:
        indegrees[near_node] -=1 
        cumuls[near_node] = max(cumuls[near_node], times[near_node] + cumuls[cur_node])
        if indegrees[near_node] == 0 :
            deq.append(near_node)

total_time = max(cumuls)
print(total_time)