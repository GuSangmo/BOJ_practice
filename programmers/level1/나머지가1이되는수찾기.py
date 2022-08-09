"""
프로그래머스 lv1 . 나머지가 1이 되는 수 찾기
"""

def solution(n):
    for i in range(1,n):
        if n%i ==1:
            answer = i
            break
    return answer