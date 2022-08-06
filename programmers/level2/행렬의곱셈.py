"""
Progarmmers Lv2. 

행렬의 곱셈
"""

"""
잘 알듯, O(N^3)으로 해결
"""


def solution(arr1, arr2):
    answer = []
    #Say, arr1: n x m, arr2: m x k    
    n , m, k = len(arr1) , len(arr1[0]), len(arr2[0])
    
    for row_idx, row in enumerate(arr1):
        new_row = []
        for col_idx in range(k):
            column = [arr2[i][col_idx] for i in range(m)]
            new_row.append(sum([i*j for i,j in zip(row,column)]))
        answer.append(new_row)
    return answer