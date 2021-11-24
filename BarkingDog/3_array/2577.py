#2577: 숫자의 개수

"""
A * B * C 에 0부터 9가 몇번 쓰였는지 

배열 만들어서 1개씩 늘림
"""

import sys
input= sys.stdin.readline

result = 1
array = [0] * 10
for _ in range(3):
    result *= int(input().rstrip())

for char in str(result):
    array[int(char)]+=1

print(*array,sep="\n")
