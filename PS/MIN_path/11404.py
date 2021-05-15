#11404. 플로이드 

"""
플로이드 워셜: O(N^3)이므로, N의 크기를 잘 보아야 한다.
모든 곳의 node를 구할때 유용하다.
"""

#Step 1. Adj matrix Initialization
"""
시작과 도착을 연결하는 노선이 여러개일 수 있음에 유의.
"""


import sys
input=sys.stdin.readline

big_num=1e9

n=int(input().rstrip())
m=int(input().rstrip())
adj_mtx=[[big_num]*n for _ in range(n)]
dist=[[big_num]*n for _ in range(n)]

for _ in range(m):
    start,end,cost=map(int,input().rstrip().split()) #효율적인 출력을 위해 zero padding은 하지 않았다.
    if adj_mtx[start-1][end-1]>0: 
        adj_mtx[start-1][end-1]=min(adj_mtx[start-1][end-1],cost) 
    else: adj_mtx[start-1][end-1]=cost
    
#Step 2. Distance Updates with O(N^3) Algorithm


#Initial Dist
for start in range(n):
    for end in range(n):
        if start==end: dist[start][end]= 0  #같은 node니까
        elif 0<adj_mtx[start][end]<big_num: dist[start][end]=adj_mtx[start][end] #초기에 설정해준 거 그대로.


#Updates:: 
#Q: 초기 로지과 다른 로직의 비교 (왜 중간에 대해서만 loop를 돌아야할까?) i,j가 fixed 된 상태에서 k에 대해 loop를 돌아야하는게 아닌가
for middle in range(n):
    for start in range(n):
        for end in range(n):
            dist[start][end]=min(dist[start][middle]+dist[middle][end] , dist[start][end])

#Step 3. Result Execution
for row in dist:
    for result in row:
        if result==big_num: result=0
        print(result,end=" ")  
    print()