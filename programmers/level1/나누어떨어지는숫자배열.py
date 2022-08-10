"""
Programmers lv1 - 나누어 떨어지는 숫자 배열
"""

def solution(arr, divisor):
    answer = [ele for ele in arr if ele%divisor == 0]
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer