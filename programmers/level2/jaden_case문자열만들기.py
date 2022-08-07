"""
Progarmmers Lv2. JadenCase 문자열 만들기

18 Min.

공백 처리때문에 힘들었으나, 하나씩 브루트포스로 하면 충분.
"""


def solution(s):
    """
    공백 문자가 관건인것 같음
    """
    
    start_flag = False 
    result_string = ""
    
    for letter in s:
        if letter.isnumeric():
            result_string += letter
            start_flag = True
            
        elif letter.isupper():
            if start_flag: #첫 문자가 아닌 경우
                result_string += letter.lower()
            else:
                start_flag = True
                result_string += letter
        
        elif letter.islower():
            if start_flag:
                result_string += letter
            else:
                start_flag = True
                result_string += letter.upper()
            
        else: # empty string
            result_string += letter
            start_flag = False
            
    return result_string
