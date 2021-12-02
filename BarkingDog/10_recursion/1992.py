#1992. 쿼드트리
"""
잘 출력하자
"""

import sys
input = sys.stdin.readline
N = int(input().rstrip())
board = [list((input().rstrip())) for _ in range(N)]

def quadtree(board, N):
    string = ""
    if N == 2: #base condition        
        result = [board[0][0],board[0][1],board[1][0],board[1][1]]
        if len(set(result)) == 1:
            return str(result[0]) 
        else:
            string = "(" + "".join(result) + ")"
            return string
    else :  #recursion 
        half = N//2 
        interval = [(0,half), (half,N)]
        previous = ""
        result ="("
        flag = True
        for (row_s,row_e) in interval:
            for (col_s,col_e) in interval:
                sub_board= [row[col_s:col_e] for row in board[row_s:row_e]] #process 된string
                sub_result = quadtree(sub_board, half) #이거 중복처리를 해야함
                
                if not previous: previous = sub_result
                elif sub_result != previous: flag = False 
                result += sub_result
        result+=")"
        #일단 이렇게 만들어놓고
        
        if flag and sub_result == "0" : result = "0"
        elif flag and sub_result == "1": result= "1"           
        return result

result = quadtree(board, N)
print(result)
    