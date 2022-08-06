"""
Progarmmers Lv2. 

N개의 최소공배수
"""

"""
유클리드 호제법을 써도 되고, math.gcd를 써도 충분하다.

while b> 0 :
    a, b = b, a%b를 기억할 것
return a

"""



from math import gcd
def lcm(a,b):
    g = gcd(a,b)
    return (a*b) // g

def solution(arr):
    prev = 1
    for idx in range(len(arr)):
        prev = lcm(prev, arr[idx])   
    return prev
