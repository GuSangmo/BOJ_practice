"""
Progarmmers Lv2. 

피보나치 수
"""

"""
5 Min
simple DP
"""


big_num = 1_234_567

def solution(n):
    dists = [-1 for _ in range(100_001)]
    dists[0] = 0
    dists[1] = 1
    for i in range(2,n+1):
        dists[i] = (dists[i-1] + dists[i-2]) % big_num
             
    answer = dists[n] %big_num
    return answer