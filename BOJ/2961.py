#2961. 도영이가 만든 맛있는 음식
"""
N = 10이니 bitmasking으로 풀 수 있음

N=1을 제외해야지!
"""

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
acids = [] ; bitters = []
for _ in range(N):
    acid, bitter = map(int,input().rstrip().split())
    acids.append(acid)
    bitters.append(bitter)
    
min_diff = 1e10

for bit in range(1,1<<N):
    total_acid = 1
    total_bitter = 0
    for k in range(N):
        if (bit & (1<<k)): 
            total_acid *= acids[k]
            total_bitter += bitters[k]
    min_diff = min(min_diff, abs(total_acid - total_bitter))
print(min_diff)
        
    