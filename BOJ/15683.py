#15683. 감시 

"""
K개의 CCTV에 대해 DFS 느낌처럼 끝까지 가고,
itertools의 product를 이용해 각 case를 brute-force로 탐색하자.

(4 **8) * 64 = 2**22 = 1000 * 1000 * 2면 충분할듯

[1] Recursion method를 썼다 
N과 M 제대로 입력받자!


[2] Rotation 비슷한걸 구현할땐 음수 인덱싱 대신 modular를 쓰자!

"""

import sys
from itertools import product
input = sys.stdin.readline


N,M = map(int, input().rstrip().split())
boards = [list(map(int,input().rstrip().split())) for _ in range(N)]


#cctv type 선언 
"""
Use recursion
"""

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def cctv(camera_type, x,y, location, result):
    # print("x,y:", x,y)
    # print("result:", result)
    if x<0 or y<0 or x>=N or y>=M : return result
    if boards[x][y] == 6 : return result   #벽은 못뚫으니깐

    nx1 = x+dx[location] ; ny1 = y+dy[location]
    nx2 = x+dx[(location-1)%4] ; ny2 = y+dy[(location-1)%4]
    nx3 = x+dx[(location-2)%4] ; ny3 = y+dy[(location-2)%4]
    nx4 = x+dx[(location-3)%4] ; ny4 = y+dy[(location-3)%4]

        
    if camera_type == 1:
        return cctv(1, nx1, ny1, location, result+[(x,y)])
    
    elif camera_type == 2:
        nx2 = x+dx[(location+2)%4] ; ny2 = y+dy[(location+2)%4]
        return cctv(1,nx1, ny1, location, result+[(x,y)])+ cctv(1, nx2,ny2,(location+2)%4,result)
    
    elif camera_type == 3:
        return cctv(1,nx1, ny1, location, result+[(x,y)])+ cctv(1,nx2,ny2,location-1,result)

    elif camera_type == 4:
        return (cctv(1,nx1, ny1, location, result+[(x,y)])+ cctv(1,nx2,ny2,location-1,result)
            + cctv(1,nx3,ny3, location-2, result))
    
    elif camera_type == 5:  
        return (cctv(1,nx1, ny1, location, result+[(x,y)])+ cctv(1,nx2,ny2,location-1,result)
            + cctv(1,nx3,ny3,location-2, result) + cctv(1,nx4,ny4, location-3, result))

#camera 정보담기
camera_dict = {}
candidates = 0
walls = 0
for row in range(N):
    rows = boards[row]
    for col in range(M):
        if rows[col]==0 : continue
        elif rows[col] == 6:  walls+=1; continue
        camera_dict[(row,col)] = rows[col] #location 위치에 camera_type 담기
        candidates +=1

possibles = list(product(range(4), repeat = candidates))


# print("camera_dict:")
# print(camera_dict)

safe_zone = 100
for case in possibles:
    result = []
    for camera_loc, value in zip(camera_dict,case):
        camera_type = camera_dict[camera_loc]
        tmp = cctv(camera_type, camera_loc[0], camera_loc[1], value, [])
        result+=tmp
        
    update_value = N*M - walls- len(list(set(result)))
    safe_zone = min(safe_zone, update_value)

    
print(safe_zone)
    









