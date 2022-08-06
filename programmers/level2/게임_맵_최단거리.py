
"""
프로그래머스 Lv2 -게임 맵 최단거리
"""

"""
5 Minute :: flood fill
"""
from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    dists = [[-1 for _ in range(M)] for _ in range(N)]
    def bfs():
        deq = deque([(0,0)])
        dists[0][0] = 1
        
        while deq:
            cur_x, cur_y = deq.popleft()
            dx = [0,0,-1,1]
            dy = [1,-1,0,0]
            for i in range(4):
                nx = cur_x + dx[i]
                ny= cur_y + dy[i]
                if nx< 0 or ny< 0 or nx>=N or ny>= M : continue
                if dists[nx][ny] >=0 or maps[nx][ny] == 0: continue 
                dists[nx][ny] = dists[cur_x][cur_y] +1 
                deq.append((nx,ny))
        return dists[-1][-1]
    
    answer = bfs()
    return answer