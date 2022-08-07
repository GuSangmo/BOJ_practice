"""
Progarmmers Lv2. N^2 배열 자르기

30 Min.

생각하는 문제
"""


#계단 형으로 0, 1, 2, ....., n이 채워져있겠네
"""
1 2 3 4 5     ............  n
2 2 3 4 5      ............  n
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5 

zero_idx기준
i행은     (i+1)가 (i+1)개    i+2 ~ N 까지 


"""


def solution(n, left, right):
    #left는 left_row 번째 행의 left_idx 번 원소 (zero_idx)
    left_row, left_idx = left // n , left % n
    right_row, right_idx = right // n , right % n
    
    #최대 10^ 7 => 40MB 라 OOM은 안 일어날 듯
    
    left_arr =  [left_row+1] * (left_row+1) +  list(range(left_row+2,n+1))
    right_arr =  [right_row+1] * (right_row+1) +  list(range(right_row+2,n+1))
    
    answer = []
    
    if left_row == right_row:
        return left_arr[left_idx: right_idx+1]
    
    answer += left_arr[left_idx:]
    for row_num in range(left_row+1, right_row):
        cur_arr = [row_num+1] * (row_num+1) + list(range(row_num+2, n+1))
        answer += cur_arr
    answer += right_arr[:right_idx+1]
    
    return answer
    
    
    