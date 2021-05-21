#2099. The Game of Death
"""
일단, 이것은 경로 문제와 다를게 없다.
서로 가르키는 것을 인접 행렬을 통해 표현하면 충분할 것.

N=200. N^3<1억. Possible.
"""
big_num=int(1e9)
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


        
#Operation Start      
#2명을 포인팅하므로..
import sys
input=sys.stdin.readline
N,K,M=map(int,input().rstrip().split())
connected_matrix=[[0]*N for _ in range(N)]
for me in range(N):
    you1,you2=map(int,input().rstrip().split())
    connected_matrix[me][you1-1]=1
    connected_matrix[me][you2-1]=1
    
final_mtx=matmul(powerMatrix(connected_matrix,K-1),connected_matrix) if K>1 else connected_matrix
    
#Result Execution
for _ in range(M):
    a,b=map(int,input().rstrip().split())
    die= (final_mtx[a-1][b-1]>=1)
    print("death" if die else "life")

    
    
    