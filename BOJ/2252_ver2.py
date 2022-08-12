#2252. 줄 세우기
"""
위상 정렬을 복습해보자.

defaultdict는 없는 값에 대해서는 default를 만들지 않을 수 있음
(search_space가 전체가 아닌데 전체에 대해 출력해야 하는 경우는 조심하자.)

시간이 많이차이나서 보니, input = sys.stdin.readline 함수를 안해놨다.
"""

import sys 
from collections import deque 
input = sys.stdin.readline
N, M = map(int,input().rstrip().split())

#For efficient indexing
graphs = [[] for _ in range(N+1)]
indegrees = [0 for _ in range(N+1)]

#그래프 생성 / indegree 배열 생성
for _ in range(M):
    start, end = map(int,input().rstrip().split())
    graphs[start].append(end)
    indegrees[end] +=1 


def topology_sort():
    # Topological sort start 
    arrs = []

    #indegree 0인 애들부터 배열에 넣음 
    deq = deque([])
    for node in range(1,N+1):
        if indegrees[node] == 0 : deq.append(node)

    while deq:
        cur_student = deq.popleft()
        arrs.append(cur_student)
        for near_student in graphs[cur_student]:
            indegrees[near_student] -= 1 
            if indegrees[near_student] == 0 :deq.append(near_student)
    return arrs 

result = topology_sort()
print(*result, end = " ")




