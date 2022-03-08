#1541.잃어버린 괄호 

"""
Parsing 후 처리.
(-)가 등장한 이후의 (+)는 모두 마이너스 처리!
"""


#Parsing

prev = ""
minus_flag = False
operations = []
for string in input().rstrip():
    if string != "-" and string!="+":
        prev +=string
    
    else:
        operations.append(int(prev))
        prev = ""
        operations.append(string)
operations.append(int(prev))
prev = ""

#Operations 

ans = 0
for operation in operations:
    if operation == "-":
        minus_flag = True 
    elif operation == "+": continue 
    
    else: 
        if minus_flag : ans -=operation
        else: ans+=operation 
print(ans)
        
        


    
        
        


