#15681. 트리와 쿼리
"""
cnt배열을 만들어서, 서브트리의 개수를 return 하는 재귀함수를 짜자




이를 위해 초기 배열 갱신은 필요할 것 같다
"""

import sys 
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1_000_000)

N, R, Q = map(int,input().rstrip().split())
graphs = [[] for _ in range(N+1)]
parents = list(range(N+1))    
subtrees = [0 for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int,input().rstrip().split())
    graphs[start].append(end)
    graphs[end].append(start)


def tree_traverse(root_node):
    deq = deque([root_node])
    while deq:
        cur_node = deq.popleft()
        for near_node in graphs[cur_node]:
            #부모 노드 제외
            if parents[cur_node] == near_node : continue 
            parents[near_node] = cur_node
            deq.append(near_node)


def get_subtree(node):
    count = 1
    for near_node in graphs[node]:
        #부모 노드 제외
        if parents[node] == near_node : continue
        count += get_subtree(near_node)
    subtrees[node] = count
    return count


#Execute and revise the parents
tree_traverse(R)
get_subtree(R)

for _ in range(Q):
    node = int(input().rstrip())
    print(subtrees[node])


