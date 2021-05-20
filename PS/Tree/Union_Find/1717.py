#1717. 집합의 표현
"""
유니온 파인드 연습 문제.

union, find 연산을 잘 구현해보자!

틀린 이유: 초기 연산-> 경로 압축 기법 X, RecursionError(limit을 설정안했음)


"""

#Parents 배열을 선언. 먼저 본인을 parents로 초기화


import sys
#재귀 overflow 방지
sys.setrecursionlimit(int(1e7))
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
parent=list(range(N+1))


#root 노드를 찾는 find 연산 (경로 압축 기법을 통한 최적화)
def find_parent(parent,x):
    if parent[x]!=x: 
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#root 노드를 비교하여 두 원소가 같은 집합에 포함되어있는지를 확인하는 union 연산
def union_parent(parent,a,b):
    a=find_parent(parent,a) #a,b 가 같으면 애초에 비교할 필요가 없긴 하지
    b=find_parent(parent,b)    
    if a<b:
        parent[b]=a
    elif a>b:
        parent[a]=b

for _ in range(M):
    order, node1, node2= map(int,input().rstrip().split())
    if order==1:
        check= (find_parent(parent,node1)==find_parent(parent,node2))
        print("YES" if check else "NO")
    elif order==0:
        union_parent(parent,node1, node2)
  