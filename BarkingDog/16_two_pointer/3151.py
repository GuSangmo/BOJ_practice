#3151. 합이 0
"""
아슬아슬하게 O(N^2) 풀이를 먼저 해보자

-> 각 loop에 대해 two pointer -> O(N^2)
"""

import sys 
from bisect import bisect_left
input = sys.stdin.readline 

N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
nums.sort()
#투 포인터
minimum = 1e10
case = 0

for idx in range(N-2):
    st = idx+1
    en = N-1
    while st<en:
        if nums[idx]+nums[st]+nums[en] >0:
            en -=1
        elif nums[idx]+nums[st]+nums[en]<0:
            st+=1
        else:
            if nums[st] == nums[en]:
                case += (en-st) * (en-st+1) //2
                break            
            new_st = st ; new_en = en
            for i in range(st,en+1):
                if nums[i] == nums[st]: new_st+=1
                else:
                    break
            for j in range(en,st-1,-1):
                if nums[j] == nums[en] : new_en-=1
                else:
                    break
            case += (new_st-st) * (en- new_en)
            st = new_st
            en = new_en    
print(case)