#9663. N-Queen
"""
N-queen에서의 state는 row로 정의한다.
row가 N까지 간 상태에서 cur == N 인지 아닌지.
"""


import sys
input = sys.stdin.readline

N = int(input().strip())

#중복 상태 check
col_visit = [False] * N  
downright_visit = [False] * (2*N+1)
upright_visit = [False] * (2*N+1)

cnt = 0
def queen(row):
    global cnt #이걸 return 안할 수는 없나
    #N-1 까지 다 채운 후, 마지막에 N이 되어서 base condition이 될 것
    if row == N:
        cnt+=1
        return 
    for col in range(N): #col : 0~ (N-1)
        #현재 위치 : (row,cur)
        if col_visit[col] or upright_visit[col+row] or downright_visit[col-row+(N-1)] : continue
        col_visit[col] = True ; upright_visit[col+row] = True ; downright_visit[col-row+(N-1)] = True
        queen(row+1)
        col_visit[col] = False ; upright_visit[col+row] = False ; downright_visit[col-row+(N-1)] = False
queen(0)
print(cnt)
    