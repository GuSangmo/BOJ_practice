#1941. 소문난 7공주
"""
seven_princess()가 담아야 할 정보는 ,

-현재 몇 번째 원소인지
-다솜파가 몇 명인지
-다솜파 위치를 담은 배열에 대한 정보 

중복을 제거해주기 위해 set()형태로 결과를 저장할 것.
"""


import sys
input = sys.stdin.readline
visit = [[False]*5 for _ in range(5)]
board = [list(input().rstrip()) for _ in range(5)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
result_dict = {}

"""
중복을 줄이는건 k=7일떄 해주자
"""
def seven_princess(k, dasom_cnt, locs):
    global result_dict
    #Base condition: 다 방문한 경우, 또는 도연파가 4명이상인 경우
    if k- dasom_cnt >=4: #글러먹음 
        return 
    if k == 7: #다 채웠다.
        if dasom_cnt>=4:
            if result_dict.get(frozenset(locs)) is None: result_dict[frozenset(locs)] = 1            
        return        
    elif k==0: #시작 조건
        for i in range(5):
            for j in range(5):
                visit[i][j] = True
                seven_princess(1, int(board[i][j]=="S"),[(i,j)])
                visit[i][j] = False
    else:
        for (row,col) in locs:
            flag = False
            """
            각 (row,col)에서 있는 후보군들의 상하좌우를 살펴본다.
            """
            for i in range(4):
                nx = row+dx[i] ; ny = col+dy[i]
                if nx<0 or nx>=5 or ny<0 or ny>= 5:continue
                if visit[nx][ny] : continue #이미 방문한 곳
                visit[nx][ny] = True            
                if board[nx][ny] == "S" : 
                    seven_princess(k+1, dasom_cnt+1, locs+[(nx,ny)])
                elif board[nx][ny] == "Y" :
                    seven_princess(k+1, dasom_cnt, locs+[(nx,ny)])           
                visit[nx][ny] = False
seven_princess(0, 0, [])
print(len(result_dict))