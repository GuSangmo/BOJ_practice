#10816 . 숫자 카드 2
"""
upper_bound와 lower_bound를 쓰면 되는데, 
이번엔 built_in이 아니라 직접 구현해보자.


이번엔 왜 start<end로 놓은걸까?

"""

import sys 
input =sys.stdin.readline 


def upper_idx(target, arr, length):
    start = 0
    end = length
    while start<end:
        mid = (start+end)//2        
        if arr[mid] > target : end = mid
        else: start = mid+1
    return start

def lower_idx(target, arr, length):
    start = 0
    end = length
    while start<end:
        mid = (start+end)//2        
        if arr[mid] >= target : end = mid
        else: start = mid+1
    return start

N = int(input().rstrip())
array = list(map(int,input().rstrip().split()))
array.sort()
M = int(input().rstrip())
targets = list(map(int,input().rstrip().split()))

for target in targets:
    result = upper_idx(target, array,N) - lower_idx(target, array, N)
    print(result, end = " ")




