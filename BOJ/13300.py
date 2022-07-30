#13300. 방 배정 
"""
A학년 B성별의 학생을 K로 나눈 뒤, 그를 올려서 배정하면 된다.

6 * 2배열을 만들자.
"""

import sys 
input = sys.stdin.readline

arrs = [[0 for _ in range(2)] for k in range(6)]
N, K = map(int,input().rstrip().split())

for _ in range(N):
    gender, grade = map(int,input().rstrip().split())
    arrs[grade-1][gender] +=1 

room = 0
for grade in range(6):
    for gender in range(2):
        candidate = arrs[grade][gender]//K
        remainder = arrs[grade][gender]%K
        if remainder == 0 :
            room += candidate   
        else: 
            room += (candidate+1) 
print(room)
    

