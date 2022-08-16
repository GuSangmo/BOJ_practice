#1463. 1로 만들기
"""
D[n] = n을 1로 만드는데 필요한 연산의 개수
"""
import sys 
input = sys.stdin.readline 
N = int(input().rstrip())
big_num = int(1e6)+1
D = [big_num for _ in range(big_num)]
D[1] = 0
for i in range(2, big_num):
    D[i] = min(D[i], D[i-1] + 1)
    if i%2 == 0 : 
        D[i] = min(D[i], D[i//2]+1)
    if i%3 == 0 : 
        D[i] = min(D[i], D[i//3]+1)
print(D[N])