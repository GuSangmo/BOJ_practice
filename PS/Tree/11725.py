#11725. 트리의 부모 찾기
"""
그래프 상에서 그냥 prev를 선언해서 풀면 안되나

풀이를 보니, 트리는 일반적인 그래프처럼 풀되 트리의 성질을 이용해서 푸는게 대부분인듯.

그니까 dfs,  bfs같은거 많이 쓰겠지.

BFS는 parents 배열을 선언해서, continue 조건이 인접한 node= cur_node의 parents 구나.

"""
import sys
from collections import deque
input=sys.stdin.readline
N=int(input().rstrip())
tree=[[] for _ in range(N+1)] 

parents=[0] * (N+1) ; parents[1]=1


#Tree 그래프로 선언하기
for _ in range(N-1):
    a,b=map(int,input().rstrip().split())
    tree[a].append(b); tree[b].append(a)


def bfs_tree(start):
    #초깃값 선언
    q=deque([])
    q.append(start)
    parents[start]=1
    while q:    
        cur_node=q.popleft()
        for near_node in tree[cur_node]:
            if parents[cur_node]==near_node: continue
            parents[near_node]=cur_node                
            q.append(near_node)
bfs_tree(1)         
for i in range(2,N+1): print(parents[i])
    
    
    
    
    
    