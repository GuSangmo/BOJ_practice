#2467. 용액
"""
0에 가까운 특성값!
"""

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
nums = list(map(int,input().rstrip().split() ))
#nums.sort()

#투 포인터
st= 0 
en = N-1
result = 1e10
while st< en :
    if abs(nums[st]+nums[en])<=result:
        ans1, ans2 = nums[st], nums[en]
    result = min(result, abs(nums[st]+nums[en]))
    if nums[st] + nums[en]< 0 :
        st +=1
    else:
        en-=1
print(ans1, ans2)