#10815.  숫자 카드
"""
Binary Search로 이용!
"""

import sys 
input = sys.stdin.readline 


#Task 1 : binary_search 구현 

def binary_search(arr, target, length):
    start = 0
    end = length-1 
    
    while start+1<end:
        mid = (start+end)//2
        if arr[mid] == target: return 1
        elif arr[mid] > target : end = mid-1 
        else : start = mid+1 

    if arr[start] == target or arr[end] == target : return 1 
    return 0


n = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
nums.sort()

m = int(input().rstrip())
targets =list(map(int, input().rstrip().split()))

for target in targets:
    print(binary_search(nums, target,n), end = " ")
