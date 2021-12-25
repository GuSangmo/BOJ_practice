#13335. 트럭
"""
deque를 이용할 것 .

다리 길이만큼의 배열을 각 원소가 0인 상태로 초기화한다. 
그 후 새로운 원소가 들어올떄마다 sum 정보를 늘리고, 
그걸 rotate시켜주면서 time을 늘리고, weight 조건을 검사한다.
"""

import sys
input = sys.stdin.readline
from collections import deque
number, length, W = map(int,input().rstrip().split())
trucks = deque(list(map(int,input().rstrip().split())))
finished = []

#Operation 

deq = deque([0 for _ in range(length)]) #각 다리의 상태정보를 저장할 배열
weight_sum = 0 # 현재 다리 위에 놓인 상태의 정보 
time = 0

def check_first(array):
    """array의 첫번째 원소가 nonzero인지 확인
    """
    return array[0]!=0

while len(finished)< number: #다 건너기 전까지 
    #상태 검사부터 하자! 
    if check_first(deq):
        out = deq.popleft()
        weight_sum -= out 
        finished.append(out)
        #새롭게 들어올 애가 있다면 넣고, 아니면 그대로
        if trucks:
            if weight_sum + trucks[0] <= W: #새롭게 넣을 수 있다면
                deq.append(trucks[0])
                weight_sum += trucks[0]
                trucks.popleft() ; time+=1
            else:
                deq.append(0)
                time+=1
        else:            
            deq.append(0)
            time+=1
    else:
        deq.rotate(-1) #그래도 회전은 시켜야지
        if trucks:
            if weight_sum + trucks[0] <= W : #새롭게 넣을 수 있다면
                deq[-1] = trucks[0]
                weight_sum += trucks[0]
                trucks.popleft() ; 
                time+=1
            else:
                time+=1
        else:
            time+=1



            
print(time)
        
        