"""
Programmers lv1 - x만큼 간격이 있는 n개의 숫자
"""

def solution(x, n):
    answer = []
    initial = x
    for loop in range(n):
        answer.append(x)
        x+= initial
    return answer