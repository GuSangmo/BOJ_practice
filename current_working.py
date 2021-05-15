#1463. 1로 만들기

"""
1로 만들때 2,3으로 나눠진다면 그건 따로 처리하는게 훨씬 효율적이다. 
"""
N=int(input())
#Step 1. Table Setting
operation=[-1]*1000001

#Step 2. Relation Setting
operation[1]=0
for i in range(N+1):
    operation[i]=operation[i-1]+1 if i>1 else 0
    if i%2==0: operation[i]=min(operation[i],operation[i//2]+1)
    if i%3==0: operation[i]=min(operation[i],operation[i//3]+1)
print(operation[N])