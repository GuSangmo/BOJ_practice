#18869. 멀티버스 2
"""
각 행성별로 좌표압축을 시킨뒤(bisect_left 이용),
이들을 각각 Counter시켜서 문제를 풀자

"""

import sys 
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
from collections import Counter
M, N = map(int,input().rstrip().split())
candidates = []

for _ in range(M):
    planets = list(map(int,input().rstrip().split()))
    compressed = tuple(bisect_left(planets, element) for element in planets)
    candidates.append(compressed)

answer = 0
for key,val in Counter(candidates).items():
    if val>=2:
        answer += val *(val-1)//2
print(answer)
