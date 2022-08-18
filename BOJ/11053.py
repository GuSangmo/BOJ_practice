#11053. LIS 
import sys 
input = sys.stdin.readline 

"""
D[j] = j까지 가장 큰 LIS의 길이

Given D[k], D[k]보다 큰 l이 있다면 

D[l] = D[k]+1

"""
import sys 
input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

D = [1 for _ in range(N)]
D[0] = 1
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]: 
            D[i] = max(D[i], D[j]+1)

print(D[-1])