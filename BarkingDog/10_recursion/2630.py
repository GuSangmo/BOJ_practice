#2630. 색종이 만들기
"""
종이의 개수와 본질적으로 동일한 문제!
"""

import sys
input = sys.stdin.readline
N = int(input().rstrip())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

def colorpaper(board, N):
    result = [0,0]
    if N == 2: #base condition        
        result[board[0][0]] +=1 ; result[board[0][1]] +=1
        result[board[1][0]] +=1 ; result[board[1][1]] +=1
        if result.count(4) >= 1:
            idx = result.index(4)
            result[idx] = 1
        return result
    else :  #recursion 
        flag = True
        half = N//2 
        interval = [(0,half), (half,N)]
        previous = ""
        for (row_s,row_e) in interval:
            for (col_s,col_e) in interval:
                sub_board= [row[col_s:col_e] for row in board[row_s:row_e]]                
                sub_result = colorpaper(sub_board, half) #이거 중복처리를 해야함
                if not previous: previous = sub_result
                elif sub_result != previous: flag = False 
                result = [i+j for i,j in zip(result, sub_result)] #각각을 더하는거죠
        
        #모든 pattern이 하나라면 합쳐야지
        if flag and result[0] == 4: result = [1,0]
        elif flag and result[1] == 4: result= [0,1]            
        return result

result = colorpaper(board, N)
print(*result, sep = "\n")
    