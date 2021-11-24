#1874 .스택 수열
"""
크게 2개의 변수를 선언한다.

s = 1~n까지의 수 중 몇까지 뽑았는가

n = 현재 만들어야 하는 수가 몇인가

이들을 top과 비교하여 코드를 짠다. 

================

s< n : n까지 push! 

- 이미 뽑지도 않았다. 그러므로 n까지 만든다!

이제 고려할 상황은 이미 s가 n보다 큰 경우
    top == n : pop()
    top != n : error가 생기는데, n을 pop해야하는 상황에서 top부터 pop하는걸론 못만드므로

"""

import sys
input = sys.stdin.readline


N = int(input().rstrip())
s = 0
stack = []
result_string = ""
flag = False
for _ in range(N):
    num= int(input().rstrip())
    while s<num:
        s+=1
        stack.append(s)
        result_string+= "+"             
    if stack[-1] == num :  
        stack.pop()
        result_string+= "-"
    else:
        flag = True
        break

if flag : print("NO")
else:     print(*list(result_string), sep="\n")