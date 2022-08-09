"""
프로그래머스 lv1 . 숫자 문자열과 영단어

-replace 여러번 쓰기
"""

def solution(s):
    change_dict = {j:i for i,j in zip(range(10), ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])}
    
    for letter, num in change_dict.items():
        s = s.replace(letter, str(num))
    
    answer = int(s)
    return answer