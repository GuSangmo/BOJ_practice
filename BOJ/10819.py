#10819. 차이를 최대로
"""
두 값의 차이를 최대로 구해야함.

[1] BF
"""

import sys 
from itertools import permutations
input = sys.stdin.readline 

def get_diff(arr):
    summation = 0
    for idx in range(len(arr)-1):
        summation += abs(arr[idx] - arr[idx+1])
    return summation

N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))

candidates = list(map(list, permutations(nums)))
answer = -1
for candidate in candidates:
    answer = max(answer, get_diff(candidate))
print(answer)