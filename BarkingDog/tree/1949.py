#1949. 우수 마을
"""
독립집합을 묻는 문제
조건 3 => 일반마을은 적어도 하나의 우수마을과 인접해 있어야 한다.
그 어느 것과도 인접해있지 않은 일반마을이 있다면, 그걸 우수마을로 색칠하면 최적해보다 커지므로 고려할 필요 없는 조건.

사회망 서비스 문제처럼, 트리 DP를 선언하여 풀자.

costs[node][1] = node가 우수 마을일 때 ==> sum(costs[near_node][0]) // 리프 노드는 모두 일반마을이어야함
costs[node][0] = node가 일반 마을일때, 리프노드는 뭐든 상관없음
"""

import sys 
input = sys.stdin.readline 
N = int(input().rstrip())
peoples = [0] + list(map(int,input().rstrip().split()))
graphs = [[] for _ in range(N+1)]
visits = [False for _ in range(N+1)]
costs = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
    c1, c2 = map(int,input().rstrip().split())
    graphs[c1].append(c2)
    graphs[c2].append(c1)

def excellent_village(node):
    visits[node] = True 
    costs[node][0] = 0
    costs[node][1] = peoples[node]
    for near_node in graphs[node]:
        if visits[near_node] : continue
        excellent_village(near_node)
        costs[node][0] += max(costs[near_node][0], costs[near_node][1])
        costs[node][1] += costs[near_node][0]
#Execute! 
excellent_village(1)
print(max(costs[1][0], costs[1][1]))