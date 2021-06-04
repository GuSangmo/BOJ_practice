#2004. 조합 0의 개수 
def count(n,k):
    cnt=0
    while n:
        n=n//k
        cnt+=n 
    return cnt

import sys
N, M=map(int, sys.stdin.readline().split())
stack_2, stack_5=0,0
stack_2=count(N,2)-count(N-M,2)-count(M,2)
stack_5=count(N,5)-count(N-M,5)-count(M,5)

print(min(stack_2, stack_5))