#2533. 사회망 서비스(SNS)
"""
costs[node][0]  = node를 색칠할 경우의 비용
costs[node][1]  = node를 색칠하지 않을 경우의 비용
"""

import sys 
input = sys.stdin.readline
sys.setrecursionlimit(100_00_0000)
N = int(input().rstrip())

costs = [[-1,-1] for _ in range(N+1)]
graphs = [[] for _ in range(N+1)]
visits = [False for _ in range(N+1)]

for _ in range(N-1):
    city1, city2 = map(int,input().rstrip().split())
    graphs[city1].append(city2)
    graphs[city2].append(city1)

def tree_traverse(node):
    """
    costs[node][0] : 본 node는 일반인 => child_node는 무조건 얼리어답터.
    costs[node][1] : 본 node는 얼리어답터 =>  child_node가 뭐든 상관없다.
    """
    visits[node] = True
    costs[node][0] = 0
    costs[node][1] = 1
    for near_node in graphs[node]:
        if visits[near_node]: continue 
        tree_traverse(near_node)
        costs[node][0] += costs[near_node][1]
        costs[node][1] += min(costs[near_node][0], costs[near_node][1])

tree_traverse(1)     
print(min(costs[1]))