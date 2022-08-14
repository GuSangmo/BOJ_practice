#4803. 트리
"""
트리의 개수 세기:: 유니온 파인드한 후에 전체 집합 개수 세면 충분할것 같은데
사이클이 보이면 사이클에 있는 것들은 -1로 바꿔준뒤,
마지막에 parent의 -1을 제외한 고유값을 세자.
N = 500이므로 재귀값 설정 필요 없음

"""

import sys 
input = sys.stdin.readline 
from collections import deque 
sys.setrecursionlimit(100_000)

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, cycle,a,b):
    root1 = find_parent(parent,a)
    root2 = find_parent(parent,b)

    if root1 == root2 or cycle[root1] or cycle[root2]:
        cycle[root1] = True 
        cycle[root2] = True
        return False

    elif root1 < root2:
        parent[root2] = root1 
        return True
    elif root1 > root2:
        parent[root1] = root2
        return True

end_flag = False
testCaseCount = 0

while not end_flag:
    testCaseCount +=1
    N, M = map(int,input().rstrip().split())
    if N == 0 and M==0 : break
    parents = list(range(N+1))

    #cycle이면 여기다 표시
    cycles = [False for _ in range(N+1)]


    #Cycle detection
    cycle_set = set()
    for _ in range(M):
        node1, node2 = map(int,input().rstrip().split())
        if not union_parent(parents, cycles, node1, node2):
            #Cycle detected
            cycle_set.add(find_parent(parents, node1))
            cycle_set.add(find_parent(parents,node2))
    
    #좋은 짓은 아니지만..
    #if cycle => 모두 -1 처리
    for node in range(1,N+1):
        parents[node] = find_parent(parents,node)
    
    for node in range(1,N+1):
        if parents[node] in cycle_set:
            parents[node] = -1

    final_result = set()
    for node in range(1,N+1):
        if parents[node]!= -1:
            final_result.add(parents[node])
    
    if len(final_result) > 1:
        print(f"Case {testCaseCount}: A forest of {len(final_result)} tress.")
    elif len(final_result) == 1:
        print(f"Case {testCaseCount}: There is one tree.")
    else:
        print(f"Case {testCaseCount}: No trees.")
    
        
        






