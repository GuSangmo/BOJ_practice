"""
Programmers lv1 - 없는 숫자 더하기
"""

def solution(numbers):
    original = set(range(10))
    answer = sum(original- set(numbers))
    return answer