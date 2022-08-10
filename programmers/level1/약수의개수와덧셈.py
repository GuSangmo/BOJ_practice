"""
Programmers lv1 - 약수의 개수와 덧셈
"""

def get_division(num):
    cnt = 0
    for divide in range(1,num+1):
        if num%divide == 0 :
            cnt+=1
    return cnt

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if get_division(num) %2 == 0 :
            answer += num
        else:
            answer -= num

    return answer