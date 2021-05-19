#16562. 친구비
"""
먼저 주어진 친구관계를 이용해서 몇 개의 집합이 있는지를 확인한다.

Union될때마다 돈을 작은 사람의 것으로 바꿔준다.

그렇게 disjoint set들 별의 돈을 합칠때 준석이의 돈보다 적다면 

친구를 사귈 수 있고, 많다면 친구를 사귀지 못하는 것.


초기 코드에서 틀린 점은 2가지.

[1] 기존의 모임에서 parent를 이용하는건 결국 root로만 비교하겠다는건데, root

[2] set이 아니라 list를 쓰는 방법이 다르다. 

한번쯤 반례를 설계해보자.


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
N,M,total_money=map(int,input().rstrip().split())
parent=list(range(N+1))

money=[0]+list(map(int,input().rstrip().split()))


#친구 네트워크 알아보기
for _ in range(M):
    friend1, friend2= map(int,input().rstrip().split())
    union_parent(parent,friend1,friend2)
    less_money=min(money[friend1], money[friend2])
    money[friend1]=less_money; money[friend2]=less_money #친구비 지출 줄여야지..

#인간관계의 뿌리가 되는 인싸 친구들이나 독고다이 넘쳐서 인생 혼자 잘사는 친구들만 추리자

inssa_friend=[parent[people] for people in range(1,N+1) if parent[people]==people]
inssa_friend_money=sum(money[inssa] for inssa in inssa_friend)
print(inssa_friend_money if inssa_friend_money<=total_money else "Oh no")