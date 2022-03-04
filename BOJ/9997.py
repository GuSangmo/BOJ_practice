#9997. 폰트
"""
Bitmasking 용! 

순수한 비트마스킹시 
(2**N) * N -> TLE....

DFS 이용해야함

"""

import sys 
N = int(input().rstrip())
bits = []

for _ in range(N):
    bit = 0
    word = input().rstrip()
    for letter in word:
        bit |= (1<<  (ord(letter)-97))
    bits.append(bit)
    
case = 0 

def visit(start, state):
    global case
    if start == N:
        if state == (1<<26)-1 : case+=1 
        return state
    else:
        return visit(start+1, state|bits[start]) + visit(start+1, state)

visit(0,0)
    
print(case)            