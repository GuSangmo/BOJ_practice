#2504. 괄호의 값
"""
VPS를 판정하면서 값을 구하면 되는 문제.
"""
import sys
input = sys.stdin.readline

isVPS = True

symbols = list(input().rstrip())
stack   = []
values  = [1] #지금 몇 배의 multiple 이 붙는지
prev = ""

result_value = 0

for symbol in symbols:
    if symbol == "(" or symbol == "[" : 
        stack.append(symbol)
        if stack[-1] =="[" : values.append(values[-1] * 3)
        else: values.append(values[-1] * 2)
        
    else:
        if not stack: isVPS = False; break
        if symbol == ")":
            #VPS인지부터 판정
            if stack[-1] == "[": isVPS = False ; break
            elif prev == "(" : #값을 구해야함
                stack.pop() #일단 없애주고
                values.pop()
                #print(f"match  2 with multiple {values[-1]}!")

                result_value += 2 * values[-1]
            else: #이미 쌓인게 있단 소리지
                stack.pop()
                values.pop()                
        elif symbol =="]":
            if stack[-1] == "(": isVPS = False; break
            elif prev=="[" : #값을 구해야함
                stack.pop()
                values.pop()
                #print(f"match 3 with multiple {values[-1]}!")
                result_value += 3* values[-1]
            else:
                stack.pop()
                values.pop()
    prev = symbol
    
    
if stack : isVPS = False
    
print(result_value if isVPS else 0)    
