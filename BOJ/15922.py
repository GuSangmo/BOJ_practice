#15922. 아우으 우아으이야!

"""
새로운 interval을 받아서 선분이 겹치면 기존 선분의 end를 갱신,
아니면 새롭게 append.

라인 스위핑의 아이디어와 어느 정도 관련이 있는 것 같다.
"""
import sys
N=int(sys.stdin.readline().rstrip())
interval_list=[]
for _ in range(N):
    start,end=map(int,sys.stdin.readline().rstrip().split())
    if not interval_list:
        interval_list.append([start,end])
    else:
        if start<=interval_list[-1][-1]: 
            interval_list[-1][-1]= max(interval_list[-1][-1],end)
        else: interval_list.append([start,end])


line_sum=sum((j-i) for i,j in interval_list) 
print(line_sum)