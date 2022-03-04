#11723. 집합
"""
비트를 이용해 T/F 값을 표현하기 때문에 풀 수 있는 문제!
비트마스킹 연습용...


Bit는 최대 20개(1~20)
"""

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())

S= 0 
for _ in range(N):
    command = input().rstrip().split()
    if command[0] == "add":
        check = int(command[1])
        check-=1
        if (S & (1<<check)): continue 
        else: 
            S |= (1<<check)
    elif command[0] == "check":
        check = int(command[1])
        check-=1
        print(int(  (S & (1<<check))!=0))
    
    elif command[0] == "remove":
        check = int(command[1])
        check-=1
        if (S & (1<<check)): 
            S &= ~(1<<check)
    elif command[0] == "toggle":
        check = int(command[1])
        check-=1
        S^= (1<<check)
    elif command[0] == "all":
        S = (1<<20)-1 
    elif command[0] == "empty":
        S = 0





