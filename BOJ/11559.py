#11559. Puyo Puyo
"""
확인해볼 것

[1] 상하좌우 탐색을 구현하는 함수

operation : visit 배열 변경 with DFS
return : 4개 이상일때 그 index들의 list를 반환 


[2] 뿌요가 터질 때 board를 바꾸는 함수

operation : 아래로 기울이는 함수 
return : 뿌요가 터진 뒤의 새로운 board

복잡도 : 18(최대 18연속 puyo) * O(NM) , enough.



First mistake: 
그냥 bfs 쓰면 된다.... 
한 방향에 집착할 필요 없음

Second mistake: 
여러 번에 하나가 터지더라도 그건 그냥 하나의 연쇄임.
ㅇㅎ ㅇㅈ

"""


#17:44

import sys
input = sys.stdin.readline
from collections import deque


#이 first_board를 가지고 연쇄적으로 작업을 할 것.
first_board = [list(input().rstrip()) for _ in range(12)]

def oob(x,y):
    return (x<0 or y<0 or x>=12 or y>=6)


dx = [-1,1,0,0]
dy = [0,0,-1,1]


puyo = 0

def bfs(board, visit, x,y):
    cnt = 0
    traceback = [(x,y)] #0으로 만들기 위함 
    visit[x][y] = True    
    deq = deque([(x,y)])    
    while deq:
        cur_x, cur_y = deq.popleft()
        cnt +=1
        for i in range(4):
            nx = cur_x+ dx[i]; ny = cur_y+dy[i] 
            if oob(nx,ny) : continue 
            if visit[nx][ny] or board[nx][ny] != board[x][y] or board[nx][ny]=="." : continue
            deq.append((nx,ny))
            traceback.append((nx,ny))
            visit[nx][ny] = True
    if cnt>=4:
        for combo_x, combo_y in traceback:
            board[combo_x][combo_y] = "."

        return True
    
    
def play_one_round(board):
    one_round_puyo = 0
    visit = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if not visit[i][j]:
                if bfs(board,visit,i,j) : 
                    one_round_puyo+=1
    if not one_round_puyo:
        return False
    return True
   
def change_arr(arr): #arr을 아래로 밀어버리는 함수
    original = []
    for element in arr :
        if element == "." : continue
        original.append(element)
    return ["." for _ in range(12-len(original))] + original
    
def change_board(board):
    """ board의 원래 값들을
    아래로 밀어서 새로운 라운드로 넘어가게 해주는
    함수를 구현하였다.    
    """
    for col in range(6):
        original_column = [board[i][col] for i in range(12)]
        changed_column = change_arr(original_column)
        for i in range(12):
            board[i][col] = changed_column[i]
    return board

end_flag = False
while not end_flag: 
    if not play_one_round(first_board):
        print(puyo)
        break
        #mutable이라 계속 변할 것 
    puyo+=1
    first_board = change_board(first_board)




"""

deq = for

u d l r u d l r 

________

uuuuuuuuuuuuuuuuuuu
봄버맨 느낌으로
ddddddddddddddddddd


--------

봄버맨인데 이제 회전을 2번 할 수 있는 



 



"""






