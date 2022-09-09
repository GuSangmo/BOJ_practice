#2228. 구간 나누기
"""
연속된 수, 구간끼리 겹쳐있으면 안됌
정확히 M개가 있어야 함.

D[idx][count]

= idx번째까지, 구간의 개수는 count일때 최대구간합


#idx를 count번째에 포함시킨다면
D[idx-1][count] + value(count)

#idx를 count번째에 포함안시킨다면
max(D[k-1][count-1]+  sum(value[k]~ value[idx])) 
"""

import sys 
input = sys.stdin.readline 
N, M = map(int, input().rstrip().split())
nums = [int(input().rstrip()) for _ in range(N)]

psums = [0]
tmp = 0
for num in nums:
    tmp += num 
    psums.append(tmp)

#DP TABLE
D = [[0 for _ in range(M+1)] for _ in range(N+1)]
for col in range(1,M+1):
    D[0][col] = -float("inf")


for idx in range(1,N+1)
    for count in range(1,M+1):
        #만약 interval 포함시
        D[idx][count] = D[idx-1][count]
        #interval 제외시 ,interval의 시작점 k를 찾아야 함
        #k가 시작점이라면,  
        for k in range(idx+1):
            if k>=2:
                D[idx][count] = max(D[idx][count], D[k-2][count-1] + psums[idx] - psums[k-1])
            elif k==1 and count==1:
                D[idx][count] = max(D[idx][count], psums[idx])

print(D[N][M])


