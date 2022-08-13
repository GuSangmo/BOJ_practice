#1976. 여행 가자
"""
200개 이하의 도시가 주어짐
각 도시의 방문여부가 주어짐.

같은 도시를 여러번 방문할 수 있으므로, union-find가 가능하다.
결국 연결요소를 찾는 것과 동일하므로.
"""

import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100000)
N = int(input().rstrip())
graphs = [[False for _ in range(N+1)] for _ in range(N+1)]
parent = [i for i in range(N+1)]

M = int(input().rstrip())

#find_parent
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    root1 = find_parent(a)
    root2 = find_parent(b)
    if root1 < root2:
        parent[root2] = root1
    elif root1 > root2:
        parent[root1] = root2


for i in range(1,N+1):
    for j,value in enumerate(map(int,input().rstrip().split()), 1):
        if value == 1:
            #Connected
            union_parent(i,j)

schedules = list(map(int,input().rstrip().split()))

schedule_parent = set(find_parent(city) for city in schedules)

if len(schedule_parent) == 1:
    print("YES")
else:
    print("NO")






