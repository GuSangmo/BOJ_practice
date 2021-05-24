#1439. 뒤집기
"""
결국 뒤집기의 최소횟수는, 
0으로만 이루어진 구간과 
1로만 이루어진 구간을 
세서 둘 중 작은 것들만 뒤집는 것이다.

구간을 세는 법: 다음 idx에서 변화가 있는지를 센다.
"""


import sys
num_list=list(map(int,list(sys.stdin.readline().rstrip())))
one_interval=0; zero_interval=0

for idx in range(len(num_list)-1):
    if idx==0:
        if num_list[idx]==1:one_interval+=1
        else: zero_interval+=1    
    if num_list[idx]!=num_list[idx+1]:
        if num_list[idx]==0:  one_interval+=1
        else: zero_interval+=1
print(min(one_interval, zero_interval))