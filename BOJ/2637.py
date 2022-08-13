#2637. 장난감 조립
"""
위상정렬에 기본적으로 필요한 

indegrees 말고도,
costs를 Counter로 대체해서 그걸 바꿔나가자
"""

import sys 
input = sys.stdin.readline
from collections import defaultdict , Counter, deque 
N = int(input().rstrip())
M = int(input().rstrip())
graphs = [[] for _ in range(N+1)]
indegrees = [0 for _ in range(N+1)]
costs = defaultdict(dict)
cumuls = defaultdict(Counter)

for _ in range(M):
    post, pre, numbers = map(int,input().rstrip().split())
    graphs[pre].append(post)
    indegrees[post] +=1
    costs[post][pre] = numbers

#Initial
deq = deque([])
defaults = []
for node in range(1,N+1):
    cumuls[node] = Counter(costs[node])
    if indegrees[node] == 0:
        deq.append(node)
        defaults.append(node)

#Topology_sort 

while deq:
    cur_node = deq.popleft()
    for near_node in graphs[cur_node]:
        how_much = costs[near_node][cur_node]
        update = {i: how_much * j for (i,j) in cumuls[cur_node].items()}
        cumuls[near_node] += Counter(update)
        indegrees[near_node] -=1 
        if indegrees[near_node] == 0 :
            deq.append(near_node)

for node in defaults:
    print(node, cumuls[N][node])