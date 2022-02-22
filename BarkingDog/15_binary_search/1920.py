#1920. 수 찾기 
"""
이진 탐색의 시작...
"""

import sys
input = sys.stdin.readline


def binary_find(target,arr, length):
    start = 0;
    end = length-1; 
    while start <= end:        
        mid = (start+end)//2 
        if arr[mid]< target:   start = mid+1
        elif arr[mid]> target: end = mid-1
        else:
            return 1
    
    return 0

N = int(input().rstrip())
arr= list(map(int,input().rstrip().split()))
M = int(input().rstrip())
checks = list(map(int,input().rstrip().split()))


#정렬 
arr.sort()
for check_element in checks:
    if binary_find(check_element, arr, N): print(1)
    else: print(0)