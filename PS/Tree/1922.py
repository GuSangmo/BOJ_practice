#1922. 네트워크 연결
"""
크루스컬 알고리즘을 이용하여 풀어보자.

이때 유니온 파인드가 쓰인다.

"""

#크루스컬 알고리즘을 위해 유니온 파인드를 구현해야함.

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a); b=find_parent(parent, b)
    if a<b: parent[b]=a
    elif a>b:parent[a]=b 
        #같은 경우는 처리 안했음.

import sys
input=sys.stdin.readline
N=int(input().rstrip())
M=int(input().rstrip())

edges=[]; TC=0 #Total cost
parent=list(range(N+1))

for _ in range(M):
    a,b,cost=map(int,input().rstrip().split())
    edges.append((cost,a,b))
    
edges.sort()


for edge in edges:
    cost, com1, com2= edge
    if find_parent(parent,com1)==find_parent(parent,com2): continue
    else:
        union_parent(parent,com1,com2)
        TC+=cost
print(TC)



