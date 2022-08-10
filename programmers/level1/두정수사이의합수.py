"""
Programmers lv1 - 두 정수 사이의 합
"""

def solution(a, b):
    if b<a:
        a,b = b,a
    answer = ((a+b) * (b-a+1)) //2
    return answer