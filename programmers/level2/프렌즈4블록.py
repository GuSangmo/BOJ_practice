"""
Progarmmers Lv2. 순위검색

좋은 문제! 효율성을 따져봤어야 했다.
10억개나 되서 그렇구나.

이분탐색을 쓰면 해결된다.

__
좋은 풀이 중에서, "-"도 애초에 넣는 방법이 있었다. 참고하자.

"""

from copy import deepcopy


def solution(m, n, board):
    gameboard = [list(tmp) for tmp in board]
    stop_condition = False 
    
    def pang_condition(board, block_type):
        pangs = set()
        for row in range(m):
            for col in range(n):
                if row+1< m-1 and col+1 <n-1:
                    if board[row][col] == board[row+1][col]\
                    == board[row][col+1] == board[row+1][col+1] == block_type:
                        pangs.union( {(row,col), (row+1, col), (row, col+1), (row+1, col+1) })
        return pangs
    
    def change_board(pangs, board):
        for row, col in pangs:
            board[row][col] = ""
        
        new_columns = []
        for col_idx in range(n):
            original_column = [board[row][col_idx] for _ in range(m)]
            #Bang 이후엔 바뀌었을 것
            afters = list("".join(original_column))
            #Padding
            new_column = ["" for _ in range(n- len(afters))] + afters
            print("previous:", original_column)
            print("after:", new_column)
            
            for row_idx in range(m):
                board[row_idx][col_idx] = new_column[row_idx]
        return board
            
    def play_one_round(board):
        blocktypes = "RMAFNTJC"
        count = 0
        pang_blocks = set()
        for block_type in blocktypes:
            pangpang = pang_condition(deepcopy(board), block_type)
            pang_blocks.union(pangpang)
        
        count +=  len(pang_blocks)
        ##Change this time
        new_board = change_board(pang_blocks, deepcopy(board))
        return count, new_board
        
        
    final_answer = 0
    while not stop_condition:
        cnt, new_board = play_one_round(gameboard)
        gameboard = new_board
        final_answer += cnt
        if cnt == 0 :
            stop_condition = True
    
    answer = final_answer
    return answer

m=4 ; n=5; board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m,n,board))