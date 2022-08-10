"""
Programmers lv1 - 가운데글자가져오기
"""

def solution(s):
    half = len(s)//2
    if len(s) % 2 == 0 :
        answer = s[half-1:half+1]
    else: # 4 => 1,2번째
        answer = s[half]

    return answer