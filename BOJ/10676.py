#10676. Cow Routing 2
"""
USACO 2015 Jan Bronze 2

최대 2개까지 쓸 수 있는데, table을 만들어서 정의!
"""

import sys
input = sys.stdin.readline
A,B,N= map(int,input().rstrip().split())
minimum_cost = 1e5
big_num = 1e5
visit_from_A = [minimum_cost] * 10001
visit_from_A[A] = 0
visit_to_B = [minimum_cost] * 10001
visit_to_B[B] = 0
for _ in range(N):
    cost, num_cities = map(int,input().rstrip().split())
    cities = list(map(int,input().rstrip().split()))
    if A in cities:
        idx1 = cities.index(A)
        for idx2 in range(idx1+1, num_cities): #그 비행기가 방문하는 도시의 개수
            city = cities[idx2]
            visit_from_A[city] = min(visit_from_A[city], cost)
    if B in cities:
        idx2 = cities.index(B)
        for idx1 in range(idx2):
            city = cities[idx1]
            visit_to_B[city] = min(visit_to_B[city], cost)

# print("visit:", visit_from_A)
# print("to:", visit_to_B)
            
cnt = 0

minimum_cost = visit_from_A[B]
flag = visit_from_A[B] <big_num
for i in range(10001):
    flag = (visit_from_A[i]< big_num) and (visit_to_B[i]<big_num)    
    if flag:
        cnt+=1
    minimum_cost = min(visit_from_A[i]+visit_to_B[i], minimum_cost)
print(minimum_cost if cnt else -1)    
