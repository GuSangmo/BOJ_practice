#16562. 친구비
"""
친구비를 줘야 하는 조건은? 
parent가 다를때겠지.
계속 최소 친구비를 꺼내야 할 것 같으므로, heapq를 쓰자.

friends = [(cost, index)] 이렇게 담자.

make_friend : friends에서 pop해가면서 , 이미 있는 root_node에 있으면 continue 
            없으면 새롭게 추가
"""

import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100_000)
import heapq 

#비용 순으로 배열을 담기
N, M, budget = map(int,input().rstrip().split())
friend_q = []
for idx, cost in enumerate(map(int,input().rstrip().split()), 1):
    heapq.heappush(friend_q, (cost,idx))

#parents 배열 선언 후 유니온-파인드
parent = list(range(N+1))

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    root1 = find_parent(a)
    root2 = find_parent(b)
    if root1 < root2:
        parent[root2] = root1
    elif root1 > root2:
        parent[root1] = root2

# parent 배열 처리를 위한 유니온-파인드 
for _ in range(M):
    a, b = map(int,input().rstrip().split())
    union_parent(a,b)

# 이제 친구비를 거두자

def make_friend(friend_pq, parent_arr, budget):
    money = 0
    friend_collection = set()
    while friend_pq:
        cost, idx = heapq.heappop(friend_pq)
        cur_root = find_parent(idx)
        if cur_root in friend_collection : continue 

        #friend_collection에 추가
        friend_collection.add(cur_root)
        money += cost 
    if money > budget:
        return "Oh no"
    else:
        return money

print(make_friend(friend_q, parent, budget))
