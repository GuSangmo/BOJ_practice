#1697. 숨바꼭질
"""
바킹독 BFS 연습문제 5 :: 숨바꼭질!

처음 제출코드가 오류가 났던 이유는 candidate에서 check해주었기 때문.
음, 이건 생각해보니 N=K 면 오류가 날 것 같다.
"""

import sys
input = sys.stdin.readline
from collections import deque

N, K= map(int,input().rstrip().split())
BIG_NUM = int(1e5)
dist = [-1] * (BIG_NUM+1)
def bfs(start):
    deq = deque([start])
    dist[start] = 0
    while deq:
        cur = deq.popleft()
        if cur == K : return dist[cur]
        candidates = [cur-1, cur+1, 2*cur]
        for candidate in candidates:
            if candidate<0 or candidate>BIG_NUM: continue
            if dist[candidate]>=0: continue
            dist[candidate] = dist[cur]+1
            deq.append(candidate)
print(bfs(N))