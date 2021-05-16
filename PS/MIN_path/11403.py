#11403. 경로 찾기
"""
인접 행렬이 주어졌으니, 초기 거리 행렬을 바로 정의하고 이를 갱신해나가자.

N=100, So enough to use Floyd-Warshall. N^3<1억.

여기선 cycle이 존재할수 있다고 판단하기 어려움.
"""

import sys
input=sys.stdin.readline

N=int(input().rstrip())
adj_mtx=[list(map(int,input().rstrip().split())) for _ in range(N)]
big_num=1e3

connected=[[big_num]*N for _ in range(N)]
#Step 1.connected matrix 초기화
for i in range(N):
    for j in range(N):
        if adj_mtx[i][j]: connected[i][j]=1

#Step 2. Connected matrix 갱신
for k in range(N):
    for i in range(N):
        for j in range(N):
            connected[i][j]=min(connected[i][j],connected[i][k]+connected[k][j])

#Step 3. Result Execution
for i in range(N):
    for j in range(N):
        print(1 if connected[i][j]<big_num else 0,end=" ")
    print()

