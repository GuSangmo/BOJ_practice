
"""
프로그래머스 Lv2 -다리를 지나는 트럭
"""

# 예전에 썼던 것. 예외 처리가 번거로웠다. 정렬이 키였는데, 앞으로 참고하기.


from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    """
    truck이 움직이는 deq를 선언하자!
    """
    truck_cnt = 0

    
    bridge_deq = deque([0 for _ in range(bridge_length)])    
    truck_deq = deque(truck_weights)
    #상태를 저장하는 변수
    
    time = 0
    cur_weight = 0
    while truck_deq: 
        finish_candidate = bridge_deq[0]
        start_candidate = truck_deq[0]
        """
        Time passes
        """
        #Can finish
        
        bridge_deq.popleft()        
        if finish_candidate > 0 :
            cur_weight -= finish_candidate
            truck_cnt += 1
        #If update available, load it!
        if cur_weight + start_candidate <= weight:
            truck_deq.popleft()
            cur_weight += start_candidate
            bridge_deq.append(start_candidate)
        elif cur_weight + start_candidate > weight:
            bridge_deq.append(0)
        time +=1
    
    #다 떠났을때
    if not truck_deq:
        while cur_weight > 0:
            candidate = bridge_deq.popleft()
            time+=1
            if candidate > 0 :
                cur_weight -= candidate
            bridge_deq.append(0)
    
    answer = time
    
    return answer