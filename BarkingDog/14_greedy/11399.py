#11399. ATM 
"""
n * P1 + (n-1) * P2 + ..... + 1* PN

P에 대해 정렬 후 답 구하기
"""

import sys 
input = sys.stdin.readline 
N = int(input().rstrip())
times =list(map(int,input().rstrip().split()))
times.sort()
ans = sum([i*j for i,j in zip(range(N,0,-1),times)])
print(ans)