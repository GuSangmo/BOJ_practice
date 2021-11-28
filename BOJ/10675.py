#10675. Cow Routing
"""
USACO 2015 Jan Bronze 1


[1] 1st Trial: 

-for 문 3개의 brute_force로 짰다. 현명하지 못했음
O(500^2 * N)
500 * 500 * N으로 비교하면 된다!

----

[2] 2nd Trial:

- 다른 사람 코드를 보니 in으로 한번에 짰다 !
- 이중 for문으로 짜는 것 같아서 훨씬 빨라진것 같다.
O(N^3을 피하니 당연한 결과같다.)


Q&A : multiple parallel 이면, 즉  O(N)을 여러개 check하면 여전히 O(N)인가? 
"""

import sys
input = sys.stdin.readline
A,B,N= map(int,input().rstrip().split())
minimum_cost = 1e9
flag = False
for _ in range(N):
    cost, num_cities = map(int,input().rstrip().split())
    cities = list(map(int,input().rstrip().split()))
    
    if (A in cities) and (B in cities) and (cities.index(A)<cities.index(B)):
        flag = True
        minimum_cost = cost if cost <= minimum_cost else minimum_cost
print(minimum_cost if flag else -1)