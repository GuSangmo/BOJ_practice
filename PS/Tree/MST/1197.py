#1197. 최소 스패닝 트리
"""
기초 MST 문제

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


V, E=map(int,input().rstrip().split())
edges=[]; Remain=0 #Total cost after removal
parent=list(range(V+1))
for _ in range(E):    
    a,b,cost=map(int,input().rstrip().split())
    edges.append((cost,a,b))
edges.sort()
for edge in edges:
    cost, com1, com2= edge
    if find_parent(parent,com1)==find_parent(parent,com2): continue
    else:
        union_parent(parent,com1,com2)
        Remain+=cost
print(Remain)


