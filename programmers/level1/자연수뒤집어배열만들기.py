"""
Programmers lv1 - 자연수 뒤집어 배열 만들기
"""

def solution(n):
    answer = list(map(int,list(str(n))[::-1]))
    return answer