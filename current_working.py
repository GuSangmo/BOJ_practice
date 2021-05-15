#1018. 체스판 다시 칠하기

#Variable Assignment, Matrix Representation

import sys
N,M= map(int, sys.stdin.readline().rstrip().split())
matrix=[] ; b=black_pattern=list("BWBWBWBW"); w=white_pattern=list("WBWBWBWB")
black_matrix=[b,w,b,w,b,w,b,w]; white_matrix=[w,b,w,b,w,b,w,b]
sliding_window_list=[] #Move this window to calculate value
for _ in range(N):
    row=list(sys.stdin.readline().rstrip())
    matrix.append(row)


##Function to calculate min.val for pattern change 
def check_diff_string(matrix):
    diff_cnt1=sum([sum(matrix[i][j]!=black_matrix[i][j] for i in range(8)) for j in range(8)])
    diff_cnt2=sum([sum(matrix[i][j]!=white_matrix[i][j] for i in range(8)) for j in range(8)])
    diff_cnt=min(diff_cnt1,diff_cnt2)
    return diff_cnt

###Operation
for x_idx in range(0,N-7):
    for y_idx in range(0,M-7):
        sliced_mtx=[row[y_idx:y_idx+8]  for row in matrix[x_idx:x_idx+8]]
        sliding_window_list.append(check_diff_string(sliced_mtx))
print(min(sliding_window_list)) 