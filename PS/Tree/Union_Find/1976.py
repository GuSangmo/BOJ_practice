#1976. 여행 가자
"""
유니온 파인드 연습 문제.

애초에 같은 집합이 아니라면 불가능하다. 

최단 비용이나 최단 경로를 구하는 것이 아니므로 유니온 파인드로 충분하다.

이건 union시에 초기 설정을 좀 잘못해줘서 초반에 몇번 틀렸었다. 주의.
"""

#Step 1. Fuctnion Setting in advance

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

        
import sys
#재귀 overflow 방지
sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline
N=int(input().rstrip())
M=int(input().rstrip())
parent=list(range(N+1))


#i번째 도시와 j번째 도시의 연결 여부를 입력받기
for first in range(1,N+1):
    cities=[0]+list(map(int,input().rstrip().split()))
    for idx in range(1,N+1):
        connect=cities[idx]
        if connect==1: union_parent(parent,first,idx) #first와 loop를 돌면서 union.
plans=list(map(int,input().rstrip().split()))
set_origin={parent[city] for city in plans}
print("YES" if len(set_origin)==1 else "NO")