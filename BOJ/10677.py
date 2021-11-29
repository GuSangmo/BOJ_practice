#10677. It's all about the base
"""
USACO 2015 Jan Bronze 3

진법을 변환하는 문제.
BF로 하기엔 힘든 점이 있으므로
투 포인터 알고리즘을 이용하였다.
"""

import sys
input = sys.stdin.readline
find = False
K= int(input().rstrip())


for _ in range(K):
    num1, num2 = list(map(int,input().rstrip().split()))
    #이 logic을 잘못짰음.
    digit1 = [num1//100, (num1//10)%10, num1%10]
    digit2 = [num2//100, (num2//10)%10,num2%10]
    arr = list(range(15001))
    start = 10 ; end = 10
    while not find :
        n1 = (digit1[0]) * (start*start) + (digit1[1]) * start + digit1[2]
        n2 = (digit2[0]) * (end*end) + (digit2[1]) * end + digit2[2]    

        if n1 == n2 : 
            print(start,end); break
        elif n1 > n2 : 
            end +=1
        else:
            start+=1
            
        
    