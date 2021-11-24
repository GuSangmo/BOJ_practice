#10808: 알파벳 개수

"""
알파벳 배열을 만들어서 입력할때마다 받는다
"""

import sys
input= sys.stdin.readline

array = [0] * 26
for char in input().rstrip():
    array[ord(char)- 97] +=1

print(*array, end= " ")
