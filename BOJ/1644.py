#1644. 소수의 연속합
"""
투 포인터 테크닉을 처음으로 배워본다.

이번에 적용시키는건 소수.

"""

#Step 1. 먼저 N보다 작은 소수를 만들자.
import sys
import math
N=int(input().rstrip())

primes=[1]*(N+1)
for i in range(2,int(math.sqrt(N))+1):
    if primes[i]==1: #아직 갱신이 안된놈
        j=2
        while i*j<=N:
            primes[i*j]=0
            j+=1

arr=[]; prime_length=0
for idx in range(2,N+1):
    if primes[idx]: arr.append(idx) ; prime_length+=1


#Step 2. 이제 두 포인터는 세팅되었다.
start=0; end=0; pSum=0

cnt=0
for start in range(prime_length): #start: 첫 인덱스부터 마지막 인덱스까지
    while pSum<N and end<prime_length:   #현재의 부분합이 M보다 작고 end를 이동시킬 여지가 있을때엔
        pSum+=arr[end]        #end를 합치고 이를 갱신
        end+=1     
    if pSum==N: cnt+=1         #만약에 뭔가 합쳐서 pSum이 넘었겠지. 같으면 추가
    pSum-=arr[start]           #이제 이번 루프는 끝이니까, start를 빼주고 다음거로 넘어가기
print(cnt)




