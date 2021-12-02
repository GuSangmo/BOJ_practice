#1074. Z

"""
배열의 위치를 4개로 쪼개서!

sub_array의 사분면에 따라 평행이동을 시켜서 1사분면(왼쪽 위)의 return값을 잘 이용해주면 된다.
"""

import sys
input = sys.stdin.readline

def visit_order(row, col, N):
    if N==1 :
        if row == 0 and col == 0  : return 0
        elif row == 0 and col == 1 : return 1
        elif row == 1 and col == 0 : return 2
        elif row == 1 and col == 1 : return 3
    else:
        half_width = 2 **(N-1)
        if row< half_width and col < half_width:
            return visit_order(row, col, N-1)
        elif row< half_width and col >= half_width:
            return (half_width *half_width) + visit_order(row, col-half_width, N-1)
        elif row>= half_width and col < half_width:
            return (half_width *half_width * 2) + visit_order(row-half_width, col, N-1)
        elif row>= half_width and col >= half_width:
            return (half_width *half_width * 3) + visit_order(row-half_width, col-half_width, N-1)
N,R,C = map(int,input().rstrip().split())
print(visit_order(R,C,N))