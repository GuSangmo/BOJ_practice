#14891. 톱니바퀴 
"""
collections.deque를 쓰면 쉽게 구현 가능할 것 같다. 
그게 아닌 방법으로도 한번 해볼 것!


데이터는 12시 방향부터 주어진다. 

[1,0,1,0,1,0,1,0]

다른것과 맞물리는 건 2번톱니바퀴와 6번 톱니바퀴이다. 

 clock1 = [1,0,1,0,1,0,1,0]

구현해야 할 것은 

각 톱니바퀴 간의 상호작용이다. 

구체적으로는, 왼쪽 톱니바퀴의 2번 index와 오른쪽 톱니바퀴의 6번 톱니바퀴를 구현시키면 된다. 
"""

import sys
input = sys.stdin.readline
from collections import deque

clocks = [list(map(int,list(input().rstrip()))) for _ in range(4)]
               
def rotate_array(array, direction):
    if direction == 1: 
        return [array[-1]]+array[:-1]
    elif direction == -1:
        return array[1:]+[array[0]]
    else:
        return array
    
              
def rotate_bfs(visit, clocks, num, direction):
    """ num 번째를 시작으로 차근차근 회전시킨다.
    """
    deq = deque([(direction,num)])
    rotates = [0,0,0,0]
    
    while deq: 
        cur_direction, cur_num = deq.popleft()
        visit[cur_num] = True
        if rotates[cur_num] == 0:
            rotates[cur_num] = cur_direction
        
        candidates = [cur_num+1, cur_num-1]
        for candidate in candidates:
            if candidate<0 or candidate>=4: continue #Idx out 
            if visit[candidate] : continue 
            
            if candidate == cur_num - 1 : # candidate의 오른쪽,  cur의 왼쪽 비교
                if clocks[candidate][2] == clocks[cur_num][6]: 
                    continue
                visit[candidate] = True
                deq.append((-cur_direction, candidate))
            
            elif candidate == cur_num + 1 : # candidate의 왼쪽,  cur의 오른쪽 비교
                if clocks[candidate][6] == clocks[cur_num][2]:

                    continue
                visit[candidate] = True
                deq.append((-cur_direction, candidate))
    for idx,rotate in enumerate(rotates):
        clocks[idx] = rotate_array(clocks[idx], rotate)
                    

K = int(input().rstrip())

final_score = 0
for _ in range(K):
    start, direction = map(int,input().rstrip().split())
    visit = [False, False, False, False]
    rotate_bfs(visit, clocks, start-1, direction)
final_score = sum(int(clocks[i][0] == 1) * (2**i) for i in range(4))
print(final_score)        
        
        
    
    

