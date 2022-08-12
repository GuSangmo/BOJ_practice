#2623. 음악프로그램
"""
안되는 경우만 따로 입력받으면 충분하다.
정렬이 안되면, 애초에 arr의 원소가 N개가 되지 못할 것.

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
    orders = list(map(int,input().rstrip().split()))
    for idx in range(1, len(orders)-1):
        prev_sing, next_sing = orders[idx], orders[idx+1]
        graphs[prev_sing].append(next_sing)
        indegrees[next_sing] +=1 


def topology_sort():
    cnt = 0
    # Topological sort start 
    arrs = []

    #indegree 0인 애들부터 배열에 넣음 
    deq = deque([])
    for node in range(1,N+1):
        if indegrees[node] == 0 : deq.append(node)

    while deq:
        cur_student = deq.popleft()
        cnt+=1
        arrs.append(cur_student)
        for near_student in graphs[cur_student]:
            indegrees[near_student] -= 1 
            if indegrees[near_student] == 0 :deq.append(near_student)
    return arrs , cnt

result, cnt = topology_sort()
if cnt < N: 
    print(0)
else:
    print(*result, sep = "\n")
