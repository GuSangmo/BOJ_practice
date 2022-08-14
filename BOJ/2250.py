#2250. 트리의 높이와 너비
"""
LC, RC Count를 받아오는 함수를 짠 후,
탐색하면서 이를 받아오자.
이때 depth 정보도 저장하기


     a 
    a   a
  a a  a  a
a    a  

root node는 lc, rc에게서 (lcs, rcs)목록을 받아 온후 
본인의 lc는 lcs+1(lc 자체), rc는 rcs+1(rc자체 받아오기)
그러면 본인이 루트라고 가정할 때 왼쪽/ 오른쪽에 노드가 얼마나 있는지를 알 수 있다.

이를 다시 root 부터 전파시킨다.
lc에게는 parent의 right_child 정보를 저장시키고,
rc에게는 parent 의 left_child 정보를 저장시킨다.
"""

import sys 
from collections import defaultdict, deque
N = int(input().rstrip())
left_childs = [-1 for _ in range(N+1)]
right_childs = [-1 for _ in range(N+1)]
parents = list(range(N+1))
informations = defaultdict(list)
graphs = [[] for _ in range(N+1)]

#Input processing
for _ in range(N):
    node, left, right = map(int,input().rstrip().split())
    left_childs[node] = left 
    right_childs[node] = right 

    if left!= -1:
        graphs[node].append(left)
        graphs[left].append(node)
    if right != -1:
        graphs[node].append(right)
        graphs[right].append(node)

#Find root 
visits = [False] * (N+1)
def bfs(cur_node):
    deq = deque([cur_node])
    while deq:
        node = deq.popleft()
        for near_node in graphs[node]:
            if visits[near_node] : continue 
            #Parent
            if left_childs[near_node] == node or right_childs[near_node] == node: 
                deq.append(near_node)
            else: continue 
    return node

        
root_node = bfs(1)

# DFS 
def dfs(node, depth):
    left_cnt = 0 
    right_cnt = 0
    if left_childs[node]!= -1:
        left_cnt = 1
        left_cnt += sum(dfs(left_childs[node], depth+1))
    if right_childs[node]!= -1:
        right_cnt = 1
        right_cnt += sum(dfs(right_childs[node], depth+1))

    informations[node] = [depth, left_cnt, right_cnt]
    return left_cnt, right_cnt

#Execute the initial
dfs(root_node, 1)

#Dfs again
def update_node(cur_node):
    deq = deque([cur_node])
    while deq:
        node = deq.popleft() 
        left, right = left_childs[node], right_childs[node]
        if left != -1:
            informations[left][2] +=  (informations[node][2] +1)
            informations[left][1] =  N -1 -informations[left][2]
            deq.append(left)
        if right!= -1:
            informations[right][1] += (informations[node][1] + 1)
            informations[right][2] =  N -1 -informations[right][1]
            
            deq.append(right)

update_node(root_node)

#Get result



results = defaultdict(lambda: [10_001,10_001])
depth_dict = defaultdict(int)
max_depth = 0
for depth, left_cnt, right_cnt in sorted(list(informations.values())):
    max_depth = max(depth, max_depth)
    origin_left, origin_right = results[depth]
    results[depth] = min(origin_left, left_cnt) , min(origin_right, right_cnt)

for depth in range(1,max_depth+1):
    depth_dict[depth] = max(depth_dict[depth], N - results[depth][1] - results[depth][0])


results = sorted(depth_dict.items(), key = lambda x: (-x[1], x[0]))
print(*results[0])
