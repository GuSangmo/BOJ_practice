#4386. 별자리 만들기
"""
이 문제에서는 L2 norm 이 정의되는데, 오차를 줄이기 위해 

마지막에 한번에 sqrt를 취해주자.

ValueError가 떴던건 float형이 아닌 int형으로 casting해서 그렇다.
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
nodes=[(0,0)]; edges=[]; Remain=0 #Total cost after removal
parent=list(range(N+1))

for _ in range(N):
    x,y=map(float,input().rstrip().split())
    nodes.append((x,y))

#N=100이니, 충분히 edges를 만들법함 (FULL CONNECT 여도 대략 5천개이므로)    
for i in range(1,N+1):
    for j in range(i+1,N+1):
        x1,y1= nodes[i]
        x2,y2= nodes[j]
        dist=((x2-x1)**2+(y2-y1)**2)**(1/2)
        edges.append((dist,i,j))

edges.sort()

for edge in edges:
    cost, com1, com2= edge
    if find_parent(parent,com1)==find_parent(parent,com2): continue
    else:
        union_parent(parent,com1,com2)
        Remain+=cost
print(round(Remain,2))


