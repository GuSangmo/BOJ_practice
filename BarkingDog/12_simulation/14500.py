#14500. 테트로미노
"""
대칭과 회전은 그냥 실제 테트리스처럼 모양을 7개 만들면 될 일.

구현해야 할 것: 

[1] 한 가지 패턴의 템플릿과 실제 board에서 공통부분을 추출하는 함수

[2] 한 가지 모양을 회전시키는 함수 

[3] 위의 함수를 일반화시켜, 여러 개의 패턴을 회전시키면서 최댓값 확인

"""

import sys
from itertools import product
input = sys.stdin.readline


pattern1 = [[1,0],[1,0],[1,1]]
pattern2 = [[0,1],[0,1],[1,1]]
pattern3 = [[1,0],[1,1],[0,1]]
pattern4 = [[0,1],[1,1],[1,0]]
pattern5 = [[0,1],[1,1],[0,1]]
squares = [[1,1],[1,1]]
long = [[1,1,1,1]]

total_patterns = [pattern1,pattern2,pattern3,pattern4,
                  pattern5]

N,M = map(int,input().rstrip().split())
board = [list(map(int,input().rstrip().split())) for _ in range(N)]


def rotate(array, direction):
    """array를 direction대로 회전시키는 함수
    """
    N = len(array) ; M = len(array[0])
    if direction%2 == 0 : 
        new_array = [[-1] * M for _ in range(N)]
        for row in range(N):
            for col in range(M):
                if direction == 0: new_array[row][col] = array[row][col]
                else:              new_array[row][col] = array[N-1-row][M-1-col]
    else:
        new_array = [[-1] * N for _ in range(M)]
        for row in range(N):
            for col in range(M):
                if direction == 1: new_array[col][N-1-row] = array[row][col]
                else:              new_array[M-1-col][row] = array[row][col]
    return new_array

def find_common_sum(x, y, board, pattern):
    r_size = len(pattern) ; c_size = len(pattern[0])
    if x+r_size >N or y+c_size >M : return 0 #Range out
    pattern_sum = 0
    for row in range(r_size):
        for col in range(c_size):
            if pattern[row][col] == 1:
                pattern_sum += board[x+row][y+col]
    return pattern_sum
                
    
def operation():
    """각 pattern별로 회전을 시켜가면서 
    주어진 테트로미노 패턴에 걸맞게 find_common_sum 수행.
    이후 최댓값을 print!
    """
    final_result = 0
    for pattern in total_patterns: # 각 pattern별로 
        for direction in range(4):
            template = rotate(pattern,direction)
            for x in range(N):
                for y in range(M):
                    common_sum = find_common_sum(x,y,board,template)
                    final_result = max(final_result, common_sum)
    for direction in range(2):
        template = rotate(long,direction)
        for x in range(N):
            for y in range(M):
                common_sum = find_common_sum(x,y,board,template)
                final_result = max(final_result, common_sum)
    template = rotate(squares,direction)
    for x in range(N):
        for y in range(M):
            common_sum = find_common_sum(x,y,board,template)
            final_result = max(final_result, common_sum)
    print(final_result)

operation()
