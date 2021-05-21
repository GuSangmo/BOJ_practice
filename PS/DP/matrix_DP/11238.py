#11238. Fibo
"""

피보나치 수와 최대공약수와 유사한 문제.


gcd(a,b)%M= gcd(a%M, b%M)이 성립하는진 사실 잘 모르겠지만..
그러지 않고선 메모리 초과가 날 것 같다.

gcd(Fib(m),Fib(n))=Fib(gcd(m,n))이라고 한다.

이에 대한 증명은 구글링을 통해 공부해보자. (재밌어보인다)


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
        return [[ ele %big_num for ele in row] for row in N ]
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
import math
input=sys.stdin.readline
T=int(input().rstrip())
for _ in range(T):
    n,m=map(int,input().rstrip().split())
    result=math.gcd(n,m)


    initial=[[0],[1]]
    matrix=[[0,1],[1,1]]

    #fib(N),fib(N+1)이 각각 있을 것

    if result==1: final_matrix=initial
    else: final_matrix=matmul(powerMatrix(matrix,result-1),initial)


    final_result=final_matrix[-1][-1]
    print(final_result)