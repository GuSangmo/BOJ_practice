
"""
프로그래머스 Lv2 -괄호 회전하기
"""

# 최대 1000번에 stack을 쓰면 충분할 듯.


def solution(s):
    answer = 0
    vps_match = {"(" : ")" , "[":"]", "{" : "}"}
    
    test = s[:]
    for i in range(len(s)):
        s = test[i:] + test[:i]
    
        stack = []
        isVPS = True
        
        for letter in s:
            if not stack :
                stack.append(letter)
                continue
            #match
            if letter in ")]}" :
                if stack[-1] not in "([{" : 
                    isVPS = False
                    break
                    
                if letter == vps_match[stack[-1]]:
                    stack.pop()
                    continue
                else:
                    isVPS = False
                    break
            else:
                stack.append(letter)    
        
        #VPS check
        if isVPS and not stack:
            answer +=1
                  
    return answer