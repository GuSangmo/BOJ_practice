#10828 .스택
"""
기초 스택 문제
"""

import sys
input = sys.stdin.readline

stack = []

N=int(input().rstrip())

for _ in range(N):
    order= input().rstrip().split()
    if order[0] == "push":
        stack.append(int(order[1]))
    elif order[0] == "top":
        print(stack[-1] if stack else -1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        print(int(bool(not stack)))
    elif order[0] == "pop":
        if stack: print(stack.pop())
        else: print(-1)