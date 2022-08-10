"""
Programmers lv1 - 최대공약수와 최소공배수
"""

def gcd(a,b):
    #유클리드
    if   b== 1 : return 1
    elif b==0: return a
    return gcd(b,a%b)

def lcm(a,b):
    g = gcd(a,b)
    return (a*b) //g

def solution(n, m):
    answer = [gcd(n,m), lcm(n,m)]
    return answer