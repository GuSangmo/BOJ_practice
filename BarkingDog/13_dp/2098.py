#2098. 외판원 순회
"""
BitMasking을 이용한 TSP문제!
"""

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
dists = [list(map(int,input().rstrip().split())) for _ in range(N)]
dp =[[-1]*(2**N) for _ in range(N)]
BIG_NUM = 1e10      

def TSP(current, visited):
    result = dp[current][visited]
    if result!= -1: 
        return result
    if visited == (1<<N) -1:
        if dists[current][0] != 0 : return dists[current][0]
        return BIG_NUM
    result = BIG_NUM
    
    
    for i in range(N):
        if (visited&(1<<i)) or dists[current][i]==0 : continue
        result = min(result, TSP(i,visited| 1<<i) + dists[current][i])
    dp[current][visited] = result
    return result 

print(TSP(0,1))


            