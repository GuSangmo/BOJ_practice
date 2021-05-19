#1947. 선물 전달
"""
본인의 선물을 본인이 아닌 사람에게 받는 경우. 

이것은 교란순열로서 모델링될 수 있다.

"""
import sys
input=sys.stdin.readline
big_num=1000000000
D=[-1]*1000001
N=int(input().rstrip())
for i in range(1,N+1):
    if i==1: D[i]=0
    elif i==2: D[i]=1
    else: D[i]= (i-1) *(D[i-1]+D[i-2]) % big_num
print(D[N])