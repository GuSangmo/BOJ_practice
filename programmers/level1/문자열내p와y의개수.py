"""
Programmers lv1 - 문자열 내 p,y의 개수
"""

def solution(s):
    s = s.lower()
    if s.count("p") == s.count("y"):
        return True
    return False