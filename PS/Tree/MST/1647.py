#1647. 도시 분할 계획
"""
이 문제에서는 도시를 2개로 나눠며, 남은 길의 유지비가 최대가 되도록 해야한다.

결국 MST라는건 N개를 spanning하기 위해 N개를 연결시키는 셈이 된다.
그 결과 생긴 edge는 N-1개인거고.


이게 N-2가 되면 멈추면 된다. 2개의 컴포넌트가 생겼을 것이므로.


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



N,M=map(int,input().rstrip().split())
edges=[]; Remain=0 #Total cost after removal
parent=list(range(N+1))

for _ in range(M):
    a,b,cost=map(int,input().rstrip().split())
    edges.append((cost,a,b))

edges.sort()

length=0
for edge in edges:
    cost, com1, com2= edge
    if length==N-2: break
    if find_parent(parent,com1)==find_parent(parent,com2): continue
    else:
        union_parent(parent,com1,com2)
        Remain+=cost
        length+=1  
print(Remain)



