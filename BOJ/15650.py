#15650. N과 M(3)
"""
이번엔 조합. 
같은 수를 여러번 골라도 되니 visit배열은 필요가 없겠다!
"""


import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
arr = [0] * M
def permutation_with_repetition(k):
    if k == M:
        print(*arr, end = " ")
        print()
        return 
    for i in range(1,N+1):
        arr[k] = i
        permutation_with_repetition(k+1)
permutation_with_repetition(0)
    