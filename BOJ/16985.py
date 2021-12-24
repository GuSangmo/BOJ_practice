#16985. Maaaaaaaaaaaaaze
"""
바킹독님 문제!

보드를 쌓는 순서, 회전하는 함수,
BFS로 total board를 탈출해주면 될 것 같다.

이를 위해, 우리는 각 board1~ board5의 정보를 dict에 저장할 것.


120(순서 정하기) * 125(BFS) * 25(배열 회전) * 1024

입구는 (0,0,0), 출구는 (4,4,4)로 놓아도 무방하다.

"""

import sys
input = sys.stdin.readline
from itertools import product, permutations,combinations
from collections import deque

#Part 1. 배열 회전을 구현하는 함수 


array_dict = {}

def rotate_array(array, direction):
    new_array = [[-1]* 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if direction == 0:
                new_array[row][col] = array[row][col]
            elif direction == 1:
                new_array[row][col] = array[4-col][row]    
            
            elif direction == 2:
                new_array[row][col] = array[4-row][4-col]
            elif direction == 3:
                new_array[row][col] = array[col][4-row]                
    return new_array

for key in range(5):
    board = [list(map(int,input().rstrip().split())) for _ in range(5)]
    array_dict[key] = board
    

    
    
#Part 2. 3차원 cube에서 BFS 하기
dh = [0,0,0,0,1,-1]
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]

def bfs(board, dist, h,x,y):    
    dist[h][x][y] = 0
    deq = deque([(h,x,y)])
    while deq:
        cur_h, cur_x, cur_y = deq.popleft()
        for i in range(6):
            nh = cur_h + dh[i]
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]            
            if nh<0 or nx<0 or ny<0 or nh>=5 or nx>=5 or ny>=5 : continue #Rangeout
            if dist[nh][nx][ny]>=0 or board[nh][nx][ny] == 0 : continue
            dist[nh][nx][ny] = dist[cur_h][cur_x][cur_y] + 1
            deq.append((nh,nx,ny))
    
    return dist[4][4][4]
    
# Part 3. 여러 개의 3차원 array를 쌓는 법 

minimal_dist = 500
normal = 0

# cube = list(array_dict.values())
# for cube_array in cube:
#     print(*cube_array, sep = "\n")
#     print()

# dist = [[[-1]*5 for _ in range(5)] for _ in range(5)]
# print(bfs(cube,dist, 0,0,0))
# print("dist")

# for each_floor in dist:
#     print(*each_floor, sep = "\n")
#     print()

for stack_case in permutations(range(5),4):
    stack_case = [0]+ list(stack_case)
    #array_dict를 어떻게 쌓을건지에 대한 순서    
    for rotation_case in product(range(4), repeat= 5):
        cube_array = []
        dist = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
                
        #큐브 갱신
        for each_floor, each_direction in zip(stack_case, rotation_case):            
            cube_array.append(rotate_array(array_dict[each_floor], each_direction))
        
        result = -1
        if cube_array[0][0][0]!= 0:    
            result = bfs(cube_array,dist,0,0,0)
            
        #결과 갱신 
        
        if result!= -1: 
            normal += 1             
            minimal_dist = min(result, minimal_dist)  
            
print(minimal_dist if normal else -1)