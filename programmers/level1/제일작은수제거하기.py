"""
프로그래머스 lv1 . 제일 작은 수 제거하기
"""

def solution(arr):
    if len(arr) <= 1:
        answer = [-1]
    else:
        arr.remove(min(arr)) 
        answer = arr
    return answer