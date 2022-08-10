"""
Programmers lv1 - 이상한문자만들기
"""

def solution(s):
    letter_flag = False
    even_flag = False
    result = ""
    for letter in s:
        if letter.isalpha(): 
            if not letter_flag :
                letter_flag = True
                even_flag = True
            if even_flag:
                result += letter.upper()
            elif not even_flag:
                result += letter.lower()
            even_flag = not even_flag
        else:
            even_flag = False
            letter_flag = False
            result += letter
            
    answer = result
    return answer