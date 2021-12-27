#2447. 별 찍기 11
"""
star의 위치에 따라서 코드가 나뉜다. 
피라미드가 크게 3가지 부분이 특징적이므로, 거기를 index삼아 해결!
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())

initial_pattern = [[" "," ","*"," "," "], [" ","*"," ","*"," "], ["*","*","*","*","*"]]


def star_print(N):
    if N == 3:
        result = initial_pattern
        return result
    else:
        half = N//2
        width = 2* N-1
        #sub_board를 정의해서, 여기서 값을 가져올 것
        prev = star_print(half)
        result = []
        for row in range(N):
            one_row = []
            for col in range(width):
                if row< half and half<= col< width-half:
                    one_row.append(prev[row][col-half])
                elif row>=half and col<N-1:
                    one_row.append(prev[row-half][col])
                elif row>=half and col>=N:
                    one_row.append(prev[row-half][col-N])
                else: one_row.append(" ")
            result.append(one_row)
        return result

result = star_print(N)

for i in range(N):
    for j in range(2*N-1):
        sys.stdout.write(result[i][j])
    sys.stdout.write("\n")

                                                              
                
                
                