
#1475: 방 번호

"""
num_set의 배열에 0~9의 숫자가 들어간 갯수를 넣을 것.
current는 현재 담을 수 있는 최대 원소의 개수.

각 자리수를 입력받을 때마다 num_set의 원소 값을 1씩 추가하여,
current보다 많으면 current를 1씩 늘린다.

이때, 6,9는 서로의 빈자리를 체크한다

#Clean code 없나 

내장함수 쓰면 python built-in을 씀.


"""

import sys
input= sys.stdin.readline
N = int(input().rstrip())
num_set= [0]* 10
current = 1

for char in str(N):
    
    if num_set[int(char)] + 1 > current : #이번에 새로 들어와서 current로 감당이 안되면 
        if char!= '6' and char!= '9':
            num_set[int(char)]+=1; current +=1
        elif char == "6":
            if num_set[9] +1 <= current: #지금 숫자가 6인데, 9에 하나를 더 넣을 수 있다면
                num_set[9] += 1
            else: num_set[6]+=1 ; current+=1        
        else: 
            if num_set[6] + 1 <= current: #지금 숫자가 9인데, 6에 하나를 더 넣을 수 있다면
                num_set[6] += 1
            else: num_set[9]+=1 ; current+=1
    else:
        num_set[int(char)] += 1
            
print(current)
