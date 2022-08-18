#10815 .숫자카드 
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
nums.sort()


def find(arr, target):
    if len(arr) == 1:
        return 1 if arr[0] == target else 0

    lo = 0 
    hi = len(arr)-1

    while lo+1 < hi:
        mid = (lo+hi)//2
        if arr[mid] > target:
            hi = mid 
        elif arr[mid] < target:
            lo =  mid
        else:
            return 1 
    
    if lo == hi:
        return 1 if arr[mid] == target else 0
    else:
        if arr[lo] ==target : return 1
        elif arr[lo+1] == target: return 1 
        else: return 0




M= int(input().rstrip())
targets= list(map(int,input().rstrip().split()))
for target in targets:
    print(find(nums,target), end = " ")
    