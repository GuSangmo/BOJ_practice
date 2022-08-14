#20955. 민서의 응급수술 
"""
유니온 파인드를 이용하여 다른 집합일때마다 connection을 끊어주고(사이클이므로)
마지막의 집합 개수만큼 다시 연결해주면 될 것 같다.
"""

import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(600_000)
N, M = map(int,input().rstrip().split())
graphs = [[] for _ in range(N+1)]
parents = list(range(N+1))

def find_parent(node):
    if parents[node] != node:
        parents[node] = find_parent(parents[node])
    return parents[node]

def union_parent(a,b):
    root1 = find_parent(a)
    root2 = find_parent(b)

    if root1 == root2:
        return False
    elif root1 < root2: 
        parents[root2] = root1 
    else: 
        parents[root1] = root2 
    return True 


connection = 0
for _ in range(M):
    city1, city2 = map(int,input().rstrip().split())
    if not union_parent(city1,city2):
        #연결을 종료시켜줌
        connection += 1 


for node in range(1,N+1):
    find_parent(node)

disjoint_sets = set()
for node in range(1,N+1):
    disjoint_sets.add(parents[node])

print("disjoint_set:" ,disjoint_sets)
#이 disjoint set들의 길이 -1 만큼 다시 연결시켜주면 된다.
connection += len(disjoint_sets) -1
print(connection)
    

