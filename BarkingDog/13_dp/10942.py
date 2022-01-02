#10942. 팰린드롬?
"""
D[i][j] = i번째에서 j번째까지가 팰린드롬인가

이를 순차적으로 update하기 위해 
term 을 맨 바깥 변수로 두고 
순차적으로 update! 
즉, 간격이 1인것 -> 2인 것-> 3인 것...순으로 update해야 
초기화된 array의 영향을 받지 않아!
"""
import sys
input = sys.stdin.readline 

N = int(input().rstrip())
D = [[0]* (N+1) for _ in range(N+1)]

numbers = [0]+ list(map(int,input().rstrip().split())) #0 : useless idx

for first in range(1,N+1):
    D[first][first] = 1
    if first <N:
        if numbers[first] == numbers[first+1]:
            D[first][first+1] = 1


for term in range(2,N+1) :  # 이것부터 채워야함.
    for start in range(1,N+1):
        end = start +term 
        if end>=N+1 : continue
        if numbers[start] == numbers[end] and D[start+1][end-1]:
            D[start][end] = 1


M = int(input().rstrip())

for _ in range(M):
    start, end = map(int, input().rstrip().split())
    print(D[start][end])