#2589. 보물섬
"""
그래프를 연결 그래프 형태로 구현한 뒤에 하면 될 것 같다.

이 문제는 그래프의 BFS를 연습하는 문제!
"""
import sys 
from collections import deque
input = sys.stdin.readline 
N = int(input().rstrip())
M = int(input().rstrip())

#연결 그래프 초기화
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int,input().rstrip().split())
    graphs[start].append(end)
    
visits = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    
#시작점에서 갈 수 있는 node들을 방문처리!
def bfs(start):
    deq = deque([start])
    visits[start][start] = 1
    while deq:
        cur_node = deq.popleft()
        for near_node in graphs[cur_node]:
            if visits[start][near_node]: continue 
            visits[start][near_node] = 1
            deq.append(near_node)

for start_node in range(1,N+1):
    bfs(start_node)
    
for start_node in range(1,N+1):
    impossible = 0
    for end_node in range(1,N+1):
        if visits[start_node][end_node] or visits[end_node][start_node]: continue 
        impossible+=1
    print(impossible)
    
