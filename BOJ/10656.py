#10656 : 십자말풀이
"""
USACO 2014 December Prob 2

Brute-force would suffice.

O(NM) * max(N,M) : 각 node별로 최대 max(N,M)번씩만 점검
(50^3)이면 충분

메모리 용량: 7500 개 저장(퍼즐, 방문 matrix 2개) -> 256MB면 충분


[1st Note]
- Board 입력받는 방법이 잘못되었음. 앞으로는 입력받는 matrix check해보기
- 예제 코드를 제대로 이해 못한 것 같다. 반드시 3칸이 아니라, 그 이상일 수 있다.

[2nd Note]
- 이후 2칸만 체크하는게 아니라, 약간 봄버맨식 느낌. 폭탄 터뜨리면 그 줄은 아예 끝.
- 따라서 visit matrix를 정의하여 방문 여부를 체크해주자
"""

import sys
input= sys.stdin.readline

#Board 입력받기
N,M= map(int,input().rstrip().split())
board = [list(input().rstrip()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
visit2 = [[0] * M for _ in range(N)]


#Rules
"""
Corner case에서 IndexError 안 뜨게 한번에 처리하면 깔끔해질텐데
"""

def horizontal_pos(i,j):
    global visit
    # python index : (i,j)
    left_condition = False
    if j >= M-2 : return False 
    if j==0 and board[i][j] == ".":
        left_condition = True    
    else:
        left_condition = board[i][j-1] == "#"
    tmp = j
    right_cnt = 0
    while tmp<M:
        if visit[i][tmp] or board[i][tmp] =="#": break
        right_cnt+=1
        visit[i][tmp] = 1
        tmp+=1
    right_condition = (right_cnt >=3) 
    
    result = left_condition and right_condition    
    return result

def vertical_pos(i,j):
    global visit2
    up_condition = False
    if i >= N-2 : return False
    if i==0 and board[i][j] == ".":
        up_condition = True
    else:
        up_condition = board[i-1][j] == "#"
    tmp = i
    down_cnt = 0
    while tmp<N:
        if visit2[tmp][j] or board[tmp][j] == "#" : break
        down_cnt+=1
        visit2[tmp][j] = 1
        tmp+=1
    down_condition = (down_cnt >=3) 

    result = up_condition and down_condition    
    return result

total = 0
stack = []
for row in range(N):
    for col in range(M):
        check = horizontal_pos(row, col) or vertical_pos(row,col)
        total+= int(check)
        if check: stack.append((row+1,col+1))
print(total)
for (i,j) in stack: print(i,j)
