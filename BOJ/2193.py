#2193. 이친수

#Step 1. Table Setting
#// D[i][j]=i자리이면서도 마지막자리가 j인 것
D=[[-1]*2 for _ in range(91)]
N=int(input())

#Step 2. Relation Setting
#// 끝자리수가 0이면, N-1자리의 끝자리수가 뭐였든 상관없음
#// 반면 1이면, N-1의 끝자리수는 무조건 0

for i in range(1,N+1):
    if i==1: D[i][0]=0; D[i][1]=1
    else: 
        D[i][0]=D[i-1][0]+ D[i-1][1]
        D[i][1]=D[i-1][0]
print(sum(D[N]))

"git test"

