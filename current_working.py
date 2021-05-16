#2660. 회장뽑기
"""
점수가 매겨지는 기준은, 각 사람들까지의 거리 중 최대값이라고 보면 된다.
모든 사람의 모든 관계에 대해서 거리를 구해야하므로, 플로이드-워셜 알고리즘을 이용하자.
"""


#Step 1. INPUT SETTING
import sys
input=sys.stdin.readline
N=int(input().rstrip())
big_num=1e2
adj_mtx=[[big_num]*N for _ in range(N)]

while 1:
    start, end=map(int,input().rstrip().split())
    if start==-1 and end==-1: break
    adj_mtx[start-1][end-1]=1
    adj_mtx[end-1][start-1]=1

for i in range(N):
    for j in range(N):
        if i==j:adj_mtx[i][j]=0
            
#Step 2. Floyd_Warshall Alg to calculate each dist.

for k in range(N):
    for i in range(N):
        for j in range(N):
            adj_mtx[i][j]=min(adj_mtx[i][j],adj_mtx[i][k]+adj_mtx[k][j])

#Step 3. Calculate each person's score.            
scores=[]

max_min=10000
for i in range(N):
    tmp=max(adj_mtx[i])
    if tmp<max_min:max_min=tmp 
    scores.append((i+1,max(adj_mtx[i])))
print(max_min)


#Step 4. 결과 처리

candidates=[]; cnt=0
for people, score in scores:
    if score==max_min: candidates.append(people); cnt+=1

        
print(max_min, cnt)
print(*candidates,end=" ")
        
