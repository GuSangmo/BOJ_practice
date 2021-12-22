#18808. 스티커 붙이기

"""
[1] 스티커를 노트북에 붙일 수 있는지 확인하는 함수를 만들자.

이를 위해, notebook array를 받아서 
스티커 크기만큼의 subarray를 파싱한다. 

그 뒤 subarray를 순회돌면서 
만약 이미 어느 칸이 차있다면 
그 스티커를 회전시킨다.
3번 회전시켜도 안 된다면 이 칸에는 옮길 수 없는 것으로,
바로 다음 위치를 알아봐야 한다.


[2] 입출력단마다 함수를 호출해주면 좋을 듯??


"""

import sys
input = sys.stdin.readline

N, M, K = map(int,input().rstrip().split())

notebook = [[0] * M for _ in range(N)]


def rotate_array(sticker):
    N,M = len(sticker), len(sticker[0])
    new_sticker = []
    for col in range(M):
        new_row = []
        for row in range(N):
            new_row.append(sticker[N-1-row][col])
        new_sticker.append(new_row)
    return new_sticker    





def comparison(notebook, row, col,sticker):
    #재귀 구조로 짜자    
    R,C = len(sticker), len(sticker[0])
    subarrays = [one_row[col:col+C] for one_row in notebook[row:row+R]]
    R2, C2 = len(subarrays), len(subarrays[0])
    if R != R2 or C!= C2 : 
        return False
    
    for i in range(R):
        for j in range(C):
            if subarrays[i][j] + sticker[i][j]>= 2: #불가능
                return False

    #된다면    
    for i in range(R):
        for j in range(C):
            notebook[row+i][col+j] += sticker[i][j]
    return True        










"""
이제 입력 처리하자
"""

sticker_cnt = 0
for num in range(K):
    R, C = map(int,input().rstrip().split())
    
    flag = False
    sticker = [list(map(int,input().rstrip().split())) for _ in range(R)]

    rotation_cnt = 0
    
    while rotation_cnt <=4:
        if flag : break
        for row in range(N):
            for col in range(M):
                if not comparison(notebook, row, col, sticker): continue 
                else:
                    flag = True
                    break        
            if flag : break
        rotation_cnt+=1
        sticker = rotate_array(sticker)
        
        
"""
스티커 개수 세기
"""
cnt = 0

for i in range(N):
    row = notebook[i]
    cnt += row.count(1)
print(cnt)
        
    
    
    
    
    
    
    
    


