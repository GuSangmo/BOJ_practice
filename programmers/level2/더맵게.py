"""
Programmers Lv 2. 더 맵게
"""

# 20 minute 

"""
파일 합치기 1과 동일함. 최소 원소가 K이상이 되도록 하는 횟수를 세면 됌
"""

import heapq

def solution(scoville, K):
    mixup = 0
    heapq.heapify(scoville)
    impossible = False
    while scoville and scoville[0]< K:
        first = heapq.heappop(scoville)
        if scoville :
            second = heapq.heappop(scoville)
            new = first + 2* second
            mixup +=1
            heapq.heappush(scoville, new)
        #이 조건을 통과 못한다면, 원소가 1개인 것
        elif first < K:
            impossible = True
            break
    if impossible :
        answer = -1
    else:
        answer = mixup
    return answer