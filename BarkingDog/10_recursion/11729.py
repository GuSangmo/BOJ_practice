#11729. 하노이탑 이동 순서

"""
N개를 옮기려면, (N-1)개를 옮긴 후 
마지막 걸 옮겨야지!
"""

import sys
input = sys.stdin.readline
operations = []
def hanoi_movement(start, end, N):
    cnt = 0 #이동 개수
    if N == 1: 
        operations.append((start, end))
        return 1
    else:
        #N-1개의 원판을 먼저 중간점에 옮기기
        cnt += hanoi_movement(start, 6-start-end, N-1)
        operations.append((start, end)) ; cnt+=1
        cnt += hanoi_movement(6-start-end, end, N-1)
        return cnt
        
K = int(input().rstrip())
cnt =hanoi_movement(1,3,K)

print(cnt)
for start, end in operations:
    print(start, end)