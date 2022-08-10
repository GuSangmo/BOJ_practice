"""
Programmers lv1 - 자릿수 더하기
"""

def solution(n):
    answer = sum(map(int,list(str(n))))
    return answer