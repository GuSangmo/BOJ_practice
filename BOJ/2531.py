#2531. 회전 초밥
"""

N, d, k, c

처음 k개의 slice를 move시킬 것임.

"""

import sys 
input = sys.stdin.readline 
from collections import deque

n, d, k,c = map(int,input().rstrip().split())

result = 0


dishes = [int(input().rstrip()) for _ in range(n)]
deq = deque(dishes[:k])

sushi_counter = {i:0 for i in list(range(1,d+1))}
sushi_counter[c] = 1

#INITIAL SETTING
start, end = 0,k-1
dishes = dishes + dishes[:k]
diff_type = 1

for element in deq:
    if sushi_counter[element]==0: 
        diff_type +=1
    sushi_counter[element] +=1  
    
while end < len(dishes)-1:
    old = deq.popleft()
    sushi_counter[old]-=1
    if sushi_counter[old]==0:
        diff_type -=1
    
    #New 
    new = dishes[end+1]
    if sushi_counter[new] ==0:
        diff_type +=1
    sushi_counter[new]+=1
    
    result = max(diff_type, result)    
    deq.append(dishes[end+1])
    
    #Break code
    end+=1
    
print(result)
    
    
    
    
    
