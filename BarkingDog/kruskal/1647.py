#1647. 도시분할 계획
"""
2개의 분할된 도시이므로, 마지막 트리 이전단계(도시 개수-2) 만큼의 연결만 있으면 충분하다.
"""
import sys 
sys.setrecursionlimit(100_000)
input= sys.stdin.readline 
end_flag = False





N, M = map(int,input().rstrip().split())
parents = list(range(N+1))
edges = []

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



for _ in range(M):
    start, end, cost = map(int,input().rstrip().split())
    edges.append((cost, start, end))

edges.sort() 
total_cost = 0
connection_cnt = 0
for cost, start, end in edges:
    if find_parent(start) != find_parent(end):
        total_cost +=cost 
        connection_cnt +=1
        union_parent(start,end)
        if connection_cnt == N-2:
            break
print(total_cost)

