"""
Programmers level2. 

기능개발 - 처음이랑 마지막 케이스 유의하기
"""
import math
def solution(progresses, speeds):
    #local maximum 뽑는 문제(이전게 크다면 그걸 그대로 가져감)
    #global maximum이 나타날때까지 계속 늘림
    durations = []
    for progress, speed in zip(progresses, speeds):
        duration = math.ceil((100-progress)/speed)
        durations.append(duration)
    
    #자기보다 왼쪽 원소중 본인보다 큰 게 얼마나 있는지를 세면 됌.
    
    local_max = -1
    cont = 0
    print("durations:", durations)
    deploys = []
    for idx, value in enumerate(durations):
        if idx == 0:
            local_max = value
            cont +=1 
            continue
        
        if local_max < value:
            local_max = value
            deploys.append(cont)
            cont = 1
            #마지막이면 그냥 추가
        else:
            cont +=1    
        
        if idx == len(durations) -1 :
            deploys.append(cont)
        
    return deploys
        