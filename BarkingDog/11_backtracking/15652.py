#15652. N과 M(4)
"""
이번엔 중복조합. 
같은 수를 여러번 골라도 되니 visit배열은 필요가 없겠다!
그러나 비내림차순이어야 한다.
"""


import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
arr = [0] * M
def permutation_with_repetition(k):
    prev = -1 if not k else  arr[k-1]
    if k == M:
        print(*arr, end = " ")
        print()
        return 
    for i in range(1,N+1):
        if i>= prev:
            arr[k] = i
            permutation_with_repetition(k+1)
permutation_with_repetition(0)
    