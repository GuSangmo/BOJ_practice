#9251. LCS
"""
패턴에 능숙해지기
"""
import sys 
input = sys.stdin.readline 
string1 = input().rstrip()
string2 = input().rstrip()
N = len(string1)
M = len(string2)

L = [[0 for _ in range(M+1)] for _ in range(N+1)]

row = 1; col = 1
for row in range(1,N+1):
    for col in range(1,M+1):
        char1 = string1[row-1]
        char2 = string2[col-1]
        if char1 == char2:
            L[row][col] = L[row-1][col-1] +1
        else:
            if L[row-1][col] > L[row][col-1]:
                L[row][col] = L[row-1][col]
            else:
                L[row][col] = L[row][col-1]
print(L[N][M])