"""
Programmers lv1 - k번쨰 수
"""

def solution(array, commands):
    answer = []
    for start, end , number in commands:
        answer.append(sorted(array[start-1:end])[number-1])
    return answer