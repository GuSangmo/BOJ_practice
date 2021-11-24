#10773 .제로
"""
pop 처리 후 마지막에 합치기
"""

import sys
input = sys.stdin.readline

stack = []

K =int(input().rstrip())
pops = 0
for _ in range(K):
    num= int(input().rstrip())
    if num: stack.append(num) 
    else: stack.pop()
print(sum(stack))