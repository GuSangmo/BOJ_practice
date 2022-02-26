#16401. 과자 나눠주기
"""
parametric search

여러 조각들을 구하는 함수를 구현후, 그걸 기반으로 이진탐색 구현.
"""


## Input

import sys
input = sys.stdin.readline

M,N = map(int,input().rstrip().split())

sticks = list(map(int,input().rstrip().split()))
max_length = max(sticks)


## Function

def get_pieces(arr, length):
    result = 0
    for element in arr:
        result+= element//length 
    return result     
    
def operation(arr, length):
    start = 1
    end = length
    
    while start+1 < end : 
        mid = (start+end)//2
        if get_pieces(arr,mid) >= M: #충분함
            start = mid
        else:
            end = mid-1
    
    if get_pieces(arr,end) >= M : return end 
    elif get_pieces(arr,start)>=M: return start 
    else: return 0 
    
    
sticks.sort()
result = operation(sticks, max_length)
print(result)