#1629. 곱셈

"""

(A^B)%C 를 구하고자 하는데,
B가 참 크다.

당연히 하나하나 구하면 
O(B) -> 21억번이라 당연히 실패.

또한 (A^B)%C = ((A%C)^B) 임을 이용하자.


"""

import sys
input = sys.stdin.readline

def get_mod(A,B,C):
    
    #Base condition
    if B == 1 : return A%C
    #홀짝에 따라 분류
    if B%2 ==0:
        return ((get_mod(A,B//2,C))**2)% C
    else:
        return  ( A* (get_mod(A,B//2,C))**2 )% C
A,B,C = map(int,input().rstrip().split())

print(get_mod(A,B,C))