#2616. 소형기관차
"""
상태 = 객차 , 소형 기관차에 있는 여부
j=0이면 소형 기관차에 포함이 안되고, j = 1,....m까지 가능하다.

D[cnt][i] =  현재 cnt번째 소형 기관차일때, i번째 객차까지 최대 몇명을 가질 수 있는가.

psum[i] = i번째까지의 prefix_sum

i가 cnt번째에 포함된다면?

==> i가 1번째  ...    D[cnt-1][i-1] + arr[i] 
==> i가 2번쨰  ,,,    D[cnt-1][i-2] + arr[i-1] + arr[i]
==> i가 3번쨰  ,,,     
==> i가 M번쨰  ,,,    D[cnt-1][i-M] + arr[i-M] + .... + arr[i]

D[cnt][i] = max( D[cnt-1][i-j] +  (psum[i] - psum[i-j]) )


i가 cnt번째에 포함되지 않는다면?
D[cnt][i] = D[cnt][i-1](이전 객차까지 최대 승객수)

"""

import sys 
input = sys.stdin.readline
N = int(input().rstrip())
psum = [0]
start_sum = 0
for element in list(map(int,input().rstrip().split())):
    start_sum+= element
    psum.append(start_sum)

max_length = int(input().rstrip())

D = [[0 for _ in range(N+1)] for _ in range(4)]


for count in range(1,4):
    for order in range(1,N+1):
        D[count][order] = max( D[count][order-1], D[count][order])
        if order-max_length >=0:
                D[count][order] = max(D[count-1][order-max_length]+ psum[order] - psum[order-max_length]
                , D[count][order]) 
print(D[3][N])
