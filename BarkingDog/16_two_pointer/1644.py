#1644. 소수의 연속합
"""
소수를 거른 후 소수로 투 포인터 알고리즘 적용!

메모리 : 1600만 byte = 16 MB

Edge case : 마지막이 되었다고 해서 굳이 없앨 필요는 없다. 

end = length인데, 그 사이 psum > N이어서 줄어들다가 답이 나올 수도 있다. 
"""

import sys 
input = sys.stdin.readline 
N = int(input().rstrip())

#소수 판별기
big_num = 4000001
candidates = list(range(big_num))
candidates[0] = 0
candidates[1] = 0

for num in range(2,2001):
    if candidates[num] == 0 : continue
    for idx in range(num*2,big_num,num):
        candidates[idx] = 0
        
primes = [i for i in candidates if candidates[i]]
length = len(primes)
psum = 0
result_cnt = 0
#투 포인터

end = 0
for start in range(length):
    while end< length and psum < N:
        psum+= primes[end]
        end+=1
    if psum == N: 
        result_cnt+=1
    psum -= primes[start]
print(result_cnt)
