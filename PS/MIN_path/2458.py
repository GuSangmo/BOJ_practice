#2458. 키 순서
"""
역사 문제(BOJ 1613)를 풀었을 때처럼,
결과적으로 갱신된 node들에 대해 big_num이 남아있다면 키 순서를 알 수 없다고 봐도 무방하다.

N=500, so time is enough.
"""

import sys
input=sys.stdin.readline

N,M=map(int,input().rstrip().split())
big_num=1e2
connected=[[big_num]*N for _ in range(N)]
#Step 1.connected matrix 초기화

for _ in range(M):
    small, big=map(int,input().rstrip().split())
    connected[big-1][small-1]=1

for i in range(N):
    for j in range(N):
        if i==j: connected[i][j]=0

#Step 2. Connected matrix 갱신
for k in range(N):
    for i in range(N):
        for j in range(N):
            connected[i][j]=min(connected[i][j],connected[i][k]+connected[k][j])

#Step 3. Result Execution
"""
일단, 이 결과로 생긴 그래프부터 봐볼까?

connected[i][j]와 connected[j][i]를 통해 선/후행 여부를 알 수 있다.

두 개 다 갱신이 안됐다면 선후행 여부를 알 수 없는 node가 있다는 소리지.
"""
cnt=0
for i in range(N):
    unknown=False
    for j in range(N):
        if connected[i][j]==big_num and connected[j][i]==big_num: 
            unknown=True
            break
    if not unknown: cnt+=1
print(cnt)        


