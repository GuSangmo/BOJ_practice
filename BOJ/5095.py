#5095. Matrix Powers
"""
그냥 modulo 연산만 구현하면 돼

그런데 출력형식이 생각보다 의외였음.

다 print한 후 마지막에 한번 더 print.
"""

#행렬 a,b가 주어졌을때 그 행렬곱을 구하는 함수
def matmul(a,b,big_num):
    row=len(a); common=len(b); column=len(b[0])
    c=[[0]*column for _ in range(row)]
    for i in range(row):
        for k in range(column):
            for j in range(common):
                c[i][k]+= a[i][j] * b[j][k]
            c[i][k]%=big_num
    return c

#분할정복을 통해 행렬의 K제곱을 구하는 함수
def powerMatrix(N,K,big_num):
    if K==1:
        return [[ele%big_num for ele in row] for row in N ]
    else:
        if K%2==0: 
            partial=powerMatrix(N,K//2,big_num)
            result=matmul(partial,partial,big_num)
            return result
        else:
            partial=powerMatrix(N,(K-1)//2,big_num)
            tmp=matmul(partial,partial,big_num)
            return matmul(tmp,N,big_num)

import sys
while 1:
    N,M,K=map(int,input().rstrip().split())
    if N==0 and M==0 and K==0: break
    mtx=[list(map(int,input().rstrip().split())) for _ in range(N)]
    final_mtx=matmul(powerMatrix(mtx,K-1,M),mtx,M) if K>1 else powerMatrix(mtx,1,M)  
    for row in final_mtx:
        for ele in row:print(ele, end=" ")
        print()
    print()
    
