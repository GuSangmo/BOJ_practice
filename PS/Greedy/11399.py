#11399. ATM
"""
첫 대기 시간은 N번, 둘째 대기 시간은 (N-1)번 ...마지막 사람 대기 시간은 1번씩 걸린다.

Total_time= N* P1+......+1*PN
이므로 P1~PN을 작은 순으로 배열하는게 맞음.

"""


import sys
N=int(sys.stdin.readline().rstrip())
num_list=sorted(list(map(int,sys.stdin.readline().rstrip().split())))
count_list=list(range(1,N+1))[::-1]
time=[i * j for i,j in zip(num_list, count_list)]
total_time=sum(time)
print(total_time)