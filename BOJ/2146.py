#2146. 다리 만들기
"""
각 island를 구분한 뒤, 각 island에서 다른 영역에 도착할때의 그 최단 거리를 구분하면 충분할 것 같다.
"""

#Part 1. island 영역 구분하기


#O(N^2) * 영역의 개수번 =>  영역 최대 1만개, sweep 가능한것도 최대 1만개


import sys 
input = sys.stdin.readline
from collections import deque , defaultdict
N = int(input().rstrip())
boards = [list(map(int,input().rstrip().split())) for _ in range(N)]
dists = [[-1 for _ in range(N)] for _ in range(N)]

def bfs(start):
    global dists
    cur_maps = []
    s_x, s_y = start

    if dists[s_x][s_y] >= 0 :
        return False , []
    dists[s_x][s_y] = 0
    deq = deque([start])

    while deq:
        cur_x, cur_y = deq.popleft()
        cur_maps.append((cur_x,cur_y))
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or ny<0 or nx>=N or ny>=N : continue 
            if dists[nx][ny] >=0: continue 
            if boards[nx][ny] ==0: continue 
            dists[nx][ny] = dists[cur_x][cur_y] + 1 
            deq.append((nx,ny))
    return True, cur_maps



cnt = 1
islands = defaultdict(list)
for row in range(N):
    for col in range(N):
        if boards[row][col] == 1:
            flag, cur_maps = bfs((row,col))
            if flag:
                islands[cnt] += cur_maps
                cnt+=1

#Part 2. 새로운 board 만든 뒤, 다른 값 나오면 다시 bfs하기 

for key in list(islands):
    for node_x, node_y in list(islands[key]):
        boards[node_x][node_y] = key

#NEW BFS

# print("BOARDS:", *boards, sep = "\n")
# print("islands:", islands)


def bfs(key):
    dists = [[-1 for _  in range(N)] for _ in range(N)]
    deq = deque(list(islands[key]))
    for cur_x, cur_y in deq:
        dists[cur_x][cur_y] = 0

    while deq:
        cur_x, cur_y = deq.popleft()
        #제일 먼저 찾은 것. 어차피 0은 포함 안시켰을테니
        if boards[cur_x][cur_y] != key and boards[cur_x][cur_y] > 0 :
            return dists[cur_x][cur_y] - 1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or ny<0 or nx>=N or ny>=N : continue 
            if dists[nx][ny] >=0: continue 
            dists[nx][ny] = dists[cur_x][cur_y] + 1 
            deq.append((nx,ny))

minimum_path_length = 1e10
for key in list(islands):
    cand_length = bfs(key)
    minimum_path_length = min(minimum_path_length, cand_length)
print(minimum_path_length)



