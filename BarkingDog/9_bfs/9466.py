#9466. 텀 프로젝트

"""
2개의 배열 

-visit 배열 
-end 배열 
을 선언하여 cycle을 탐지한다.
"""

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global visit , end, choose
    deq = deque([start])
    visit[start] = 1
    
    cycle = 0
    
    while deq:
        #cycle을 찾기전까지는 최대한 pop해보자
        cur = deq[0]
        new = deq[-1]
        choice = choose[new]
        
        
        """
        종료 조건
        
        -원소가 하나인 사이클 : new와 choice가 같다?
        
        -원소가 여러개인 사이클 : cur와 choice가 같다?
        """
                
        if new == choice: #하나인 사이클 찾았다!
            end[new] = 1
            deq.pop() #new제거
            while deq:
                end[deq.popleft()] = 0 #그 하나 cycle이 아니면 끝이니까.
            return 1    
        
        if visit[choice]:
            if end[choice] == -1 : 
                end[choice] = 1
                while deq and deq[0] != choice:
                    end[deq.popleft()] = 0
                #그러면 남은 애들은 cycle이겠지
                while deq:
                    end[deq.popleft()] = 1
                    cycle+=1
                return cycle
            
            ##이외의 경우는 어떡하지

            else:
                return 0
        visit[choice] = 1  #먼저 end를 갱신할 필요는 없지.
        deq.append(choice)

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    visit = [0] * (N+1)   #1번학생부터 셀 것이므로 조심
    end   = [-1] * (N+1)
    choose = [0] + list(map(int,input().rstrip().split()))
    cycle = 0
    for start_node in range(1,N+1):
        if not visit[start_node] : cycle+=bfs(start_node)
    result = N - cycle
    print(result)
    
    


