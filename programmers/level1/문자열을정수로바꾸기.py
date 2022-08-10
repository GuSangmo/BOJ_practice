"""
Programmers lv1 - 문자열을정수로바꾸기
"""

def solution(s):
    if s[0] == "+":
        return int(s[1:])
    elif s[0] == "-":
        return - int(s[1:])
    else:
        return int(s)