"""
Programmers lv1 - 문자열 다루기 기본
"""

def solution(s):
    answer = (len(s) in [4,6]) and (s.isnumeric())
    return answer