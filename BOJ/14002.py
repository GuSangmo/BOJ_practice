#14002. LIS 4
"""
D[i] = LIS의 길이 
prev[i] = i 이전의 LIS
"""
import sys 
input = sys.stdin.readline
N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))

D = [1 for _ in range(N)]
prev = [-1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            if D[i] < (D[j]+1) :
                prev[i] = j
                D[i] = D[j]+1

maximum = max(D)
print(maximum)

idx = D.index(maximum)
arrs = []
while idx != -1:
    arrs.append(nums[idx])
    idx = prev[idx]
print(*arrs[::-1])
