#12850. 본대 산책 2

"""
인접 행렬을 K번제곱하면 K개의 간선을 거쳐서 그 점에 도착하는 경로의 개수가 나옴.
"""

big_num=1000000007
#행렬 a,b가 주어졌을때 그 행렬곱을 구하는 함수
def matmul(a,b):
    row=len(a); common=len(b); column=len(b[0])
    c=[[0]*column for _ in range(row)]
    for i in range(row):
        for k in range(column):
            for j in range(common):
                c[i][k]+= a[i][j] * b[j][k]
            c[i][k]%=big_num
    return c

#분할정복을 통해 행렬의 K제곱을 구하는 함수
def powerMatrix(N,K):
    if K==1:
        return [[ele%big_num for ele in row] for row in N ]
    else:
        if K%2==0: 
            partial=powerMatrix(N,K//2)
            result=matmul(partial,partial)
            return result
        else:
            partial=powerMatrix(N,(K-1)//2)
            tmp=matmul(partial,partial)
            return matmul(tmp,N)

#Operation start
import sys
input=sys.stdin.readline

mtx=[[0,1,1,0,0,0,0,0],[1,0,1,1,0,0,0,0],[1,1,0,1,1,0,0,0],[0,1,1,0,1,1,0,0],[0,0,1,1,0,1,1,0],[0,0,0,1,1,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,0,1,1,0]]
D=int(input().rstrip())
final_result=matmul(powerMatrix(mtx,D-1),mtx) if D>1 else mtx

time=final_result[0][0]
print(time)
