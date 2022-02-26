#2230. 수 고르기
"""
Two-pointer 연습문제
"""

import sys 
input = sys.stdin.readline 

N, M = map(int,input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(N)]
arr.sort()

#Two pointer 
end = 0
minimum = 1e10

for start in range(N):
    while end<N and arr[end]-arr[start]<M: 
        end+=1
    if end == N : break
    minimum = min(minimum, arr[end]-arr[start])
print(minimum)
    