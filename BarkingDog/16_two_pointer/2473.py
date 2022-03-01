#2473. 세 용액
"""
0에 가까운 특성값인데, 이제 세 용액 버전!
Two pointer + Binary_search
--> No. 이 풀이는 Two pointer의 loop 버전!

"""

import sys 
from bisect import bisect_left
input = sys.stdin.readline 

N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
nums.sort()

#투 포인터
minimum = 1e10
for idx in range(N):
    st = idx+1
    en = N-1 
    while st<en:
        if abs(nums[idx]+nums[st]+nums[en])<minimum:
            answer = [nums[idx], nums[st], nums[en]]    
            minimum = abs(nums[idx]+nums[st]+nums[en])
        if nums[idx]+nums[st]+nums[en]> 0: 
            en -=1
        else:
            st +=1

print(*answer, sep = " ")