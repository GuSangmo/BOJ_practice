"""
Programmers Lv 2. 짝지어 제거하기
"""

"""
문자열의 길이가 100만이므로, 스택을 사용해 풀었음
"""


# 6 minute

def solution(s):
    """
    문자열 폭발과 비슷하다. 
    원소를 한번에 담은 후, 들어올때마다 마지막 원소가 같은지를 확인한다.
    """
    
    stack = []
    for letter in s:
        if not stack:
            stack.append(letter)
            continue
        
        #Top 값이랑 같은지 확인하고, 같으면 pop시킨 후 continue
        #다르다면 stack에 넣기
        if stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    answer = int(not bool(stack))

    return answer