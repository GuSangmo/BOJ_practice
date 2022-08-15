#16236. 아기 상어
"""
시뮬레이션 게임. 아기 상어는 얼마나 살아남을 수 있는가.

기록해야할 것
- map에 있는 물고기의 정보
- 현재 상어의 몸 크기

"""

# 1. Input processing

import sys 
input = sys.stdin.readline
import heapq 
from collections import deque

boards = []
fish_set = set()

N = int(input().rstrip())

for row in range(N):
    numbers = list(map(int,input().rstrip().split()))
    for col in range(N):
        if 1<=numbers[col]<= 6: fish_set.add( (row,col))
        elif numbers[col] == 9 : initial_shark_position = (row,col)
    boards.append(numbers)
#
# Helper function
#

def bfs_with_fish(start, shark_size):
    s_x, s_y = start 
    deq = deque([start])
    dists = [[-1 for _ in range(N)] for _ in range(N)]
    dists[s_x][s_y] = 0
    candidate_dist = 1e10
    candidates = []
    while deq:
        cur_x, cur_y = deq.popleft()
        if (cur_x,cur_y) in fish_set and  0< boards[cur_x][cur_y] <shark_size :
            candidate_dist = dists[cur_x][cur_y]
            candidates.append((candidate_dist, cur_x, cur_y))

        if dists[cur_x][cur_y] > candidate_dist : 
            #candidates 이상의 거리는
            continue

        dx  = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx<0 or ny<0 or nx>= N or ny>= N : continue 
            if dists[nx][ny] >= 0 : continue 
            if boards[nx][ny] > shark_size : continue 
            dists[nx][ny] = dists[cur_x][cur_y] + 1
            deq.append((nx,ny))
    
    #BFS가 끝난 후 정렬해서 판단
    candidates.sort()

    #끝내야함
    if not candidates: 
        return -1 , -1, -1
    distance, target_row, target_col = candidates[0]
    return distance, target_row, target_col
#
# Round_play :: 매 round마다 answer을 찾되, 실제로 이동하는 과정에서 불가능하면 바로 반환
#

def play_round(fish_set, start_pos):
    global boards
    shark_size = 2
    flag = True
    elapsed_time = 0
    shark_pos = start_pos
    how_much = 0
    while flag:
        shark_row, shark_col = shark_pos
        distance, target_row, target_col = bfs_with_fish(shark_pos, shark_size)
        if distance == -1:
            #더는 먹을 물고기가 없음
            return elapsed_time

        
        #먹은거 하나 추가, 및 업데이트
        how_much += 1
        if how_much == shark_size:
            shark_size += 1 
            how_much = 0

        #시간 업데이트, 위치 업데이트, 지도 업데이트 , 물고기 정보 업데이트
        elapsed_time += distance
        boards[shark_row][shark_col] = 0
        boards[target_row][target_col] = 9
        shark_pos = (target_row, target_col)
        fish_set.remove((target_row,target_col))
        


survival_time = play_round(fish_set, initial_shark_position)
print(survival_time)