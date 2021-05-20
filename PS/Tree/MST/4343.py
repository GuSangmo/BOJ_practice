#4343. Arctic Network
"""
결국 P개의 node를 모두 Tree하는 MST가 필요할 것인데,

Satellite로 연결이 가능한 애들이 있기 때문에 N-S-1개만 연결하면 될 것 같음.

이때, 마지막으로 연결된 edge의 길이가 D가 되어야 한다.

사소한 아이디어때문에 틀렸음.

이상한 자료가 답이 될 수도 있다. (기존 코드를 리뷰해보면 알 것.)

length를 올리는 과정에서 마지막이 되는걸 동시에 처리해주면 된다.

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



test_cases=int(input().rstrip())
for _ in range(test_cases):
    S, P=map(int,input().rstrip().split())
    nodes=[(0,0)]; edges=[]; 
    Remain=0 #Total cost after removal
    parent=list(range(P+1))

    for _ in range(P):    
        x,y=map(float,input().rstrip().split())
        nodes.append((x,y))

#N=500이니, 충분히 edges를 만들법함 (FULL CONNECT 여도 대략 25만개이므로)    
#마지막 연결 채널의 길이가 답임.
    for i in range(1,P+1):
        for j in range(i+1,P+1):
            x1,y1= nodes[i]
            x2,y2= nodes[j]
            dist=((x2-x1)**2+(y2-y1)**2)**(1/2)
            edges.append((dist,i,j))
    edges.sort()
    length=0
    for edge in edges:
        cost, com1, com2= edge
        if find_parent(parent,com1)==find_parent(parent,com2): continue
        else:
            union_parent(parent,com1,com2)
            Remain+=cost
            length+=1
            if length==P-S: print("{0:0.2f}".format(cost));break #Done


