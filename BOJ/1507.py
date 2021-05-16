#1507. 궁금한 민호
"""
그동안 푼 것과는 역발상인 문제. 
주어진 최단거리가 분해한 결과와 달랐다면, 그걸 새롭게 edge였다고 바라보면 될 것 같음.

removed란 배열을 만들어, 거리가 갱신될때마다 쓸데없는 node라는 표시를 해준다.
(i,j)와 (k,j)의 합에 의해 만들어질 수 있으므로.

그렇게 removed되지 않은 것들만 남긴다. 이때 i==k거나 k==j이면 거리가 0이라 강제 remove되니 
얘네는 pass.

출력에 "불가능한 경우"라는 문구가 제시되어있는데 이것을 못봤다. 

이미 주어진 행렬이 최단거리라는 가정이 되어있기에, 

i-> j >> i->k + k->j 라면 이건 모순이다. 
이 경우에는 impossible_flag를 선언해주어 따로 -1을 출력시켜주었다.

"""

import sys
input=sys.stdin.readline

N=int(input().rstrip())
big_num=1e2
dist=[list(map(int,input().rstrip().split())) for _ in range(N)]
#Step 1.connected matrix 초기화

removed=[[False]*N for _ in range(N)]
span=[]; total=N**2
impossible_flag=False
for k in range(N):
    for i in range(N):
        for j in range(N):
            if removed[i][j]: continue
            if i==k or k==j: continue
            if dist[i][j]==dist[i][k]+dist[k][j]: #갱신되었단 소리.
                removed[i][j]=True
            elif dist[i][j]>dist[i][k]+dist[k][j]:
                impossible_flag=True
                
                
for i in range(N):
    for j in range(i,N): #중복해서 들어갈 수 있으니까. i->j, j->i.
        if not removed[i][j]: span.append(dist[i][j])
                
print(sum(span) if not impossible_flag else -1)