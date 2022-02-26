#2467. 용액 
"""
정확히 무얼 비교하고자 하는지. 

lp = x< target인 원소의 개수 


"""

import sys 
input = sys.stdin.readline
from bisect import bisect_left, bisect_right


def bisect_except(arr, target, index, length):
    lp = bisect_left(arr, target)
    rp = bisect_right(arr, target)
    candidates = [] #거리를 비교할 것들을 담는다. 
    #이미 제일 큰 것임 ㅋㅋ

    if lp != rp:
        return -abs(target), abs(target)
        
    if arr[-1]< 0:     return arr[-2], arr[-1]
    elif arr[0]>0:     return arr[0], arr[1]
    
    if lp == index: #InRange
        if lp+1<length:
            candidates.append((lp+1,arr[lp+1]))
        candidates.append((lp-1,arr[lp-1]))
        
    elif lp-1 == index: #InRange
        if lp>=2:
            candidates.append((lp-2, arr[lp-2]))        
        if lp<length:
            candidates.append((lp, arr[lp]))
    else:  #안 겹침
        if lp == N:
            candidates.append((lp-1, arr[lp-1])) 
        else:
            candidates.append((lp, arr[lp])) 
            candidates.append((lp-1, arr[lp-1])) 
        
    # print(f"original idx: {index}, target:{target}")
    min_dist = 1e11
    answer = -1
    for cand_idx, cand_value in candidates:
        # print(f"cand_idx: {cand_idx}, cand_value: {cand_value}")
        if abs(cand_value - target) <min_dist:
            min_dist = cand_value - target 
            answer = cand_value 
    
    pair1, pair2 = min(answer, -target), max(answer, -target)
    return pair1, pair2 



N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
final_dist = 1e11

fpair1, fpair2 = -1,-1
for idx, value in enumerate(nums):
    pair1, pair2 =  bisect_except(nums, -value, idx, N)
    # print("pair1, pair2:", pair1, pair2)
    # print("sum:",abs(pair1+pair2))
    if abs(pair1+ pair2) < final_dist:
        final_dist = abs(pair1+pair2)
        fpair1, fpair2 = pair1, pair2
print(fpair1, fpair2)
        
    
    
    