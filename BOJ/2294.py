#2294. 동전 2
"""
knapsack DP처럼 최적화시키되, split할때그걸 더함.
"""
import sys 
input = sys.stdin.readline 
N, K = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(N)]

#1차원 배열을 쓴다면
big_num = int(1e7)
D = [big_num for _ in range(K+1)] 
for coin in coins:
    for money in range(1,K+1):
        if money == coin : 
            D[money] = 1
        elif money > coin:
            D[money] = min(D[money-coin] + D[coin], D[money])

print(D[K] if D[K] != big_num else -1)
