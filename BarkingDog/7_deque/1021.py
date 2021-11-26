#1021. 회전하는 큐
"""
각 원소가 index의 어디에 위치하는지를 파악하여 앞쪽에 가까운지, 
뒷쪽에 가까운지를 확인한다.
"""
import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().rstrip().split())
deq = deque(list(range(1,N+1)))
nums = list(map(int,input().rstrip().split()))

operation_cnt = 0
size = N
for num in nums:
    find = False
    while not find:
        num_idx = deq.index(num)
        if num_idx == 0 : #찾았음
            deq.popleft() #뽑았으니
            size -= 1
            find = True
            break
        elif num_idx <= size//2:
            operation_cnt+= num_idx
            deq.rotate(-num_idx)
        else:
            operation_cnt += (size- num_idx)
            deq.rotate(size-num_idx)
print(operation_cnt)