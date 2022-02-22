#18870. 좌표 압축
"""
중복 제거 후 해보자!
"""

import sys 
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))

ordered_nums = list(set(nums))
ordered_nums.sort()

for number in nums:
    cnt = bisect_left(ordered_nums,number)
    print(cnt, end = " ")



