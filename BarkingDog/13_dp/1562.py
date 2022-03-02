#1562. 계단 수 
"""
길이가 N이면서 0부터 9까지 모두 등장하는 계단 수

New Concept:: BitMasking 을 이용!

D[i][j][visit] -> i자리수, j로 끝나는 수, 방문상태는 visit(Bitmask)

Memory : 100 * 10 * 1024 = 4 * 10^6 -> 4MB

Time : O(N * 10 * 1024) / N<100 : Possible

갱신 순서 : visit을 각각 처리하고, 그다음 j로 가는게 맞는듯 

비트보다 덧셈, 뻴셈이 우선순위가 높음에 유의.
"""
big_num = 1_000_000_000
import sys 

D = [[[0] * (2**10) for _ in range(10)] for _ in range(101)]

for j in range(1,10): 
    D[1][j][1<<j]=1

for i in range(2,101):
    for j in range(10):
        for visit in range(1024):
            if j != 0:
                D[i][j][visit|1<<j] += D[i-1][j-1][visit]
            if j != 9 : 
                D[i][j][visit|1<<j] += D[i-1][j+1][visit]
N = int(input().rstrip())
result = sum(D[N][j][(1<<10)-1] for j in range(10)) %big_num
print(result)





