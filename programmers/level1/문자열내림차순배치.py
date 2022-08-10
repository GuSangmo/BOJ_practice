"""
Programmers lv1 - 문자열 내림차순 배치
"""

def solution(s):
    new_list = sorted(list(s), key = lambda x: ord(x))[::-1]
    answer = "".join(new_list)
    return answer