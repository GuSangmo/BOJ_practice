#4386. 별자리 만들기
"""
N개를 만들면 충분
"""
import sys 
sys.setrecursionlimit(100_000)
input= sys.stdin.readline 
end_flag = False





N = int(input().rstrip())
parents = list(range(N))
points = []
for _  in range(N):
    x,y = map(float,input().rstrip().split())
    points.append((x,y))

edges = []
for idx1 in range(N):
    for idx2 in range(idx1+1, N):
        x1, y1 = points[idx1]
        x2, y2 = points[idx2]
        dist = ((x2-x1) **2 + (y2-y1)**2) **(0.5)
        edges.append((dist, idx1, idx2))

edges.sort()

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



total_cost = 0
connection_cnt = 0
for cost, start, end in edges:
    if find_parent(start) != find_parent(end):
        total_cost +=cost 
        connection_cnt +=1
        union_parent(start,end)
        if connection_cnt == N-1:
            break
print(round(total_cost,3))

