#6497. 전력난
"""

"""
import sys 
input= sys.stdin.readline 
end_flag = False

# 유니온 파인드 함수 구현
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a,b):
    root1 = find_parent(parents, a)
    root2 = find_parent(parents, b)
    if root1 < root2:
        parents[root2] = root1 
    elif root1 > root2:
        parents[root1] = root2 


original_cost = 0
while not end_flag:
    M,N = map(int,input().rstrip().split())
    if M==0 and N==0 : break
    parents = list(range(M+1))
    
    edges = []
    for _ in range(N):
        start, end, cost = map(int,input().rstrip().split())
        edges.append((cost, start, end))
        original_cost +=cost

    edges.sort() 
    total_cost = 0
    connection_cnt = 0
    for cost, start, end in edges:
        if find_parent(parents, start) != find_parent(parents, end):
            total_cost +=cost 
            connection_cnt +=1
            union_parent(parents, start,end)

            if connection_cnt == M-1:
                break
    
    saved_cost = original_cost - total_cost
    print(saved_cost)

