"""
Programmers level2. 

괄호변환 - 이해하는데 시간이 더 오래걸렸다.
"""

def isvalid(p):
    stack = []
    for symbol in p:
        if not stack:
            if symbol == ")":
                return False
            else:
                stack.append(symbol)
            continue
        if symbol == stack[-1]:
            stack.append(symbol)
        else: #")"이 들어옴
            stack.pop()
    if stack:
        return False
    return True

def separate(p):
    open_cnt = 0 ; close_cnt = 0
    u = "" ; v = ""
    for idx, symbol in enumerate(p):
        if symbol == "(":
            open_cnt +=1
        elif symbol == ")":
            close_cnt +=1
        
        if open_cnt == close_cnt:
            compare_idx = idx
            u = p[:compare_idx+1]
            v = p[compare_idx+1:]
            break
    return u, v

def solution(p):
    answer = ''
    
    if isvalid(p) or len(p) == 0:
        return p
    
    else:
        u, v = separate(p)    
        if isvalid(u):
            answer = u+ solution(v)
        else:
            answer = "(" + solution(v) + ")"
            for idx, string in enumerate(u):
                if idx == 0 or idx == len(u)-1 : continue
                if string == "(":
                    answer +=")"
                else:
                    answer +="("

    return answer