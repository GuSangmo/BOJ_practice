"""
Programmers lv1 - 수박
"""

def solution(n):
    answer = '수박' * (n//2) + "수박"[:n%2]
    return answer