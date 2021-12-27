#14499. 주사위 굴리기
"""
cube의 정보를 세 개의 배열에 담는다.

LR = [top, right, under, left] 
UD = [top, left, under, front]
FB = [front, left, back, right]


[1] Idea 확인
[2] rotate시킬때 잘못했음
[3] 문제를 똑바로 안 읽었음.

"""

import sys
input = sys.stdin.readline

N,M,x,y,K = map(int,input().rstrip().split())

boards = [list(map(int,input().rstrip().split())) for _ in range(N)]

commands = list(map(int,input().rstrip().split()))




dx = [0,0,1,-1]
dy = [1,-1,0,0]




direction_dicts = {1:"R", 2:"L", 3:"U", 4:"D"}
operation_pos_dicts = {i:j for (i,j) in zip(list("RLUD"),[(0,1),(0,-1),(-1,0),(1,0)])}

def rotate_cube(board, lr, ud, fb, x,y,direction):
    dx, dy = operation_pos_dicts[direction]
    nx = x+ dx
    ny = y+ dy
    top, right, under, left = lr
    back = ud[1]
    front = ud[-1]
    if nx<0 or ny<0 or nx>=N or ny>=M : 
        return False, (lr,ud,fb), (x,y)
    flag = True
    while flag:
        if direction == "R": #right
            lr = [lr[-1]] +lr[:-1]
            ud = [left,back,right,front]
            fb = [front,under,back,top]
        elif direction == "L" : # left 
            lr = lr[1:]+[lr[0]]
            ud = [right,back,left,front]
            fb = [front,top,back,under]
        elif direction == "D": # Down
            lr = [back,right,front,left]
            ud = [back,under,front,top]
            fb = [top,left,under,right]
        elif direction == "U": #Up
            lr = [front,right,back,left]
            ud = [front,top,back,under]
            fb = [under,left,top,right]
        flag = False
    if board[nx][ny]!= 0 : 
        under = board[nx][ny]
        lr[2] = under
        ud[2] = under
        board[nx][ny] = 0
        
    elif board[nx][ny] == 0 :
        board[nx][ny] = lr[2]
            
    return True, (lr,ud,fb), (nx,ny)


lr = [0,0,0,0] ; ud = [0,0,0,0] ; fb = [0,0,0,0]

for command in commands: 
    operation = direction_dicts[command]
    flag, (lr, ud, fb), (x,y) = rotate_cube(boards,lr,ud,fb,x,y,operation)    
    if not flag :        continue
    print(lr[0])







    
        