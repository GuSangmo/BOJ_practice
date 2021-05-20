#4195. 친구 네트워크
"""
친구 네트워크에 변화를 관찰하는 문제.

유니온 파인드가 일어날때마다 그 수를 더하면 되는 문제.

이때 초기의 세팅이 중요하다.

if element in array...라는 형식이 O(N)이라 불편하긴 하지만,

시간이 넉넉하니 일단 해보자.

문자열로 input을 받는 것이 익숙하지 않았다. 
둘째로 if element in array...라는 입력이 좀 불편했으나 제한시간 때문에 그냥 넘어갔음.

"""

#Step 1. Fuctnion Setting in advance

#root 노드를 찾는 find 연산 (경로 압축 기법을 통한 최적화)
def find_parent(parent,x):
    if parent[x]!=x: 
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#root 노드를 비교하여 두 원소가 같은 집합에 포함되어있는지를 확인하는 union 연산
def union_parent(parent,number,a,b):
    a=find_parent(parent,a) #a,b 가 같으면 애초에 비교할 필요가 없긴 하지
    b=find_parent(parent,b)
    if a!=b:
        parent[b]=a #루트 갱신
        number[a]+=number[b]
    return number[a]
        
import sys
#재귀 overflow 방지
sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline
T=int(input().rstrip())
for _ in range(T):
    F=int(input().rstrip())
    parent={}
    number={}
    for _ in range(F):
        p1, p2= input().rstrip().split()
        if p1 not in parent: parent[p1]=p1; number[p1]=1
        if p2 not in parent: parent[p2]=p2; number[p2]=1
        res=union_parent(parent,number,p1,p2)
        print(res)
    
    
    
    
