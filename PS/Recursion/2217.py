#1629. 곱셈
"""
이것은 분할정복(DnC)과도 관련이 있는 문제, 
a%b의 O(N)은 일반적으로 O(a/2) 미만.
"""

#a**b mod C를 구할때, b가 너무 크다면 어떻게 해야할까?
import sys
input=sys.stdin.readline
def get_mod(a,b,c):
    #Base condition:
    if b<=2: return ((a%c)**b)%c
    else:
        if b%2==0: return ((get_mod(a,b//2,c))**2)%c
        else: return ((get_mod(a,b//2,c))**2 * (a%c))%c

A,B,C=map(int,input().rstrip().split())
print(get_mod(A,B,C))