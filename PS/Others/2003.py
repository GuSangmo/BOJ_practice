#2003. 수들의 합 2
"""
투 포인터 테크닉을 처음으로 배워본다.
"""

import sys
N,M=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))
#두 포인터 세팅
start=0; end=0; pSum=0

cnt=0
for start in range(N): #start: 첫 인덱스부터 마지막 인덱스까지
    while pSum<M and end<N:   #현재의 부분합이 M보다 작고 end를 이동시킬 여지가 있을때엔
        pSum+=arr[end]        #end를 합치고 이를 갱신
        end+=1     
    if pSum==M: cnt+=1         #만약에 뭔가 합쳐서 pSum이 넘었겠지. 같으면 추가
    pSum-=arr[start]           #이제 이번 루프는 끝이니까, start를 빼주고 다음거로 넘어가기
print(cnt)




