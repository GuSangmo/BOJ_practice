"""
프로그래머스 lv1 . 내적
"""

def solution(a, b):
    answer = sum(i*j for i,j in zip(a,b))
    return answer