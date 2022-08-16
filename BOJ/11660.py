#11660 .구간합 구하기 5
"""
전부 구해놓고 시작해야함.
row_wise로 다 더하면 TLE뜬다. (최대 O(N) * M)
psum(row,col) = (1,1)부터 row,col까지 left_diagnoal의 합
"""


import sys 
input = sys.stdin.readline
N, M= map(int,input().rstrip().split())
arr = [list(map(int,input().rstrip().split())) for _ in range(N)]


psum = [[0 for _ in range(N+1)] for _ in range(N+1)]
for row in range(1,N+1):
    for col in range(1,N+1):
        psum[row][col] = psum[row][col-1] + psum[row-1][col] - psum[row-1][col-1] + arr[row-1][col-1]

#Part 2. Execute 

for _ in range(M):
    x1,y1, x2,y2 = map(int,input().rstrip().split())
    partial_sum = psum[x2][y2] - psum[x2][y1-1] - psum[x1-1][y2] + psum[x1-1][y1-1]
    print(partial_sum)


