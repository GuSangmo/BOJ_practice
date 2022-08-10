"""
Programmers lv1 - 시저 암호
"""

def solution(s, n):
    answer = ''
    upper_key = {i:j for i,j in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))}
    lower_key = {i:j for i,j in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()))}
    
    for string in s:
        if string.isupper():
            start_idx = ord(string) - ord("A")
            end_idx = (start_idx + n)%26
            answer += upper_key[end_idx]
            #상대적 간격 : Z
        elif string.islower():
            start_idx = ord(string) - ord("a")
            end_idx = (start_idx + n)%26
            answer += lower_key[end_idx]

        else:
            answer += string
    return answer