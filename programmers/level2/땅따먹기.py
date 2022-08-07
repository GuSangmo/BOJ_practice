"""
Progarmmers Lv2. 땅따먹기

10 Min.

Simple DP
"""


def solution(land):
    N = len(land)
    costs = [[-1 for _ in range(4)] for _ in range(N)]
    #
    # costs[i][j] = (i,j에서 출발했을 때 얻는 최고점수)
     #


    for row in range(N)[::-1]:
        for col in range(4):
            if row == N-1:
                costs[row][col] = land[row][col]
            else:
                for candidate in [(col+1)%4, (col+2)%4, (col+3)%4]:
                    costs[row][col] = max(costs[row+1][candidate] + land[row][col], costs[row][col])
    answer = max(costs[0])

    return answer