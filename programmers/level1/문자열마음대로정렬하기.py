"""
Programmers lv1 - 문자열마음대로정렬하기
"""

def solution(strings, n):
    answer = sorted(strings, key = lambda x: (x[n],x))
    return answer