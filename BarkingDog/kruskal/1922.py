#1922. 네트워크 연결
"""
크루스컬 알고리즘::

edge를 cost 순으로 sort한 후, union_find가 다르면 add! 
같으면 continue

edges 를 일단 다 담는다. 정렬한 후, 
union_find를 시행한 후, parent가 같지 않으면 합친다.
"""
import sys 
input= sys.stdin.readline 

N = int(input().rstrip())
M = int(input().rstrip())
parents = list(range(N+1))

# 유니온 파인드 함수 구현
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(a,b):
    root1 = find_parent(a)
    root2 = find_parent(b)
    if root1 < root2:
        parents[root2] = root1 
    elif root1 > root2:
        parents[root1] = root2 
    
edges = []
for _ in range(M):
    start, end, cost = map(int,input().rstrip().split())
    edges.append((cost, start, end))

edges.sort() 
total_cost = 0
for cost, start, end in edges:
    if find_parent(start) != find_parent(end):
        print("start-end connected:", start, end)
        total_cost +=cost 
        union_parent(start,end)
    else:
        continue

print(total_cost)

