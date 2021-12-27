#1182. 부분수열의 합
"""
부분수열에서의 합이 S인지 아닌지를 check하는 문제.
state는 그걸 포함하고 있냐 아니냐로 정의.
"""


import sys
input = sys.stdin.readline

N,S = map(int,input().strip().split())

#중복 상태 check
visit = [False] * N
cnt = 0
arr = list(map(int,input().rstrip().split()))
def subseq_sum(arr_num,total_sum):
    global cnt
    if arr_num == N:
        if total_sum == S:
            cnt+=1
        return 
    subseq_sum(arr_num+1, total_sum);
    subseq_sum(arr_num+1, total_sum + arr[arr_num])
subseq_sum(0,0)

if S == 0 : cnt-=1
print(cnt)
    