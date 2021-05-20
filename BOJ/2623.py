#2623. 음악프로그램
"""
위상정렬을 연습해보는 문제.
"""

#indegree(진입차수) 배열을 정의.

#그래프 세팅
import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())

indegree=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    number, *orders=list(map(int,input().rstrip().split()))
    for idx in range(number-1):
        cur=orders[idx]; next_one=orders[idx+1]
        graph[cur].append(next_one)
        indegree[next_one]+=1

def topology_sort(total):
    result=[]
    q=deque()
    length=0
    isCycle=False
    for i in range(1,N+1):
        if indegree[i]==0: q.append(i)    
    while q:
        cur_node=q.popleft(); length+=1
        result.append(cur_node)
        for near_node in graph[cur_node]: 
            indegree[near_node]-=1
            if indegree[near_node]==0: q.append(near_node)
    
    if length<N: isCycle=True
    if not isCycle:
        for i in result: print(i)
    else: print(0)
    
topology_sort(N)


