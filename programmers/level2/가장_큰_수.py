"""
Programmers Lv 2. 가장 큰 수
"""

"""
수들을 string 형태로 max_length만큼 만들어 비교 후, sort하여 풀면 충분하다.
단 input이 0일 수 있음을 유의한다.
"""


# 10 minute 

def process(string):
    digits = list(string)
    return (digits * 4)[:4]

def solution(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers.sort(key = lambda x: process(str(x)))
    answer = str(int("".join(numbers[::-1])))
    return answer