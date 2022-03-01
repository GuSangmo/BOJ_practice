#1806. 부분합
"""
부분합 중 S가 되는걸 받는다!
"""

import sys 
input = sys.stdin.readline
N, S = map(int,input().rstrip().split())
tmp = list(map(int,input().rstrip().split()))

#Prefix sum : 부분합으로 만들어놓기 
psum = [0]
tot = 0
for ele in tmp:
    tot +=ele
    psum.append(tot)
    
    
#Two pointer 
"""
psum[end]-psum[start]>=S면, 이미 end에서 더 갱신할 필요가 없지. 
그러면  start+=1을 늘리면 돼

"""
end = 0
min_length = 1e8
flag = False
for start in range(N):
    while end <= N and psum[end] - psum[start]<S:
        end+=1 
    if end == N+1 : break 
    flag = True
    min_length = min(min_length, end-start)
    
print(min_length if flag else 0)
        