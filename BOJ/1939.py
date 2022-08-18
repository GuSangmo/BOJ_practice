#1756.
"""
피자 굽기
==>  딱 자기보다 작은 애에서 걸릴 것임
==> 배열을 정렬하며 내림차순으로 만들어주면 충분
"""

import sys 
input = sys.stdin.readline 
D, N = map(int,input().rstrip().split())
nums = list(map(int,input().rstrip().split()))

#내림차순 배열 dough 선언
doughs = []
for idx, dough in enumerate(nums):
    if idx == 0: 
        doughs.append(dough)
    else:
        doughs.append(min(dough, doughs[idx-1]))

#직접 구현하는 parametric search
def find_height(arr, target, limit= D-1):
    lo = 0 
    hi = limit
    while lo+1 < hi:
        mid = (lo+hi)//2
        if arr[mid] > target: #뚫고 들어감
            lo = mid
        elif arr[mid] < target: #여기는 무조건 막히는 곳
            hi = mid
    #arr[lo] > target, arr[hi] < target이 되도록 구성했으므로
    if arr[lo] >= target and arr[lo+1] < target: #여기 직전
        return lo
    elif arr[lo] < target:
        return lo-1

pizzas = list(map(int,input().rstrip().split()))

for pizza in pizzas:
    print(find_height(doughs, pizza))