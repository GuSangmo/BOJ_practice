#11501. 주식 
"""
마지막부터 순차적으로 뒤집으면서 local_max를 갱신하면 된다! 
그리고 그 차액만큼 더하면 돼!
"""

import sys 
input = sys.stdin.readline 

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    prices = list(map(int,input().rstrip().split()))[::-1]
    local_maximum_lists = []
    cur_max = -1

    for element in prices:
        if element >=cur_max:
            cur_max = element
        local_maximum_lists.append(cur_max)

    ans = sum([j-i for i,j in zip(prices, local_maximum_lists)])
    print(ans)
