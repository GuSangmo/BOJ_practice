#9019 .DSLR

"""
1번쨰 시도 : 데크 이용해서 구현 -> 비효율적이었나 봄. 
그냥 하자.

2번째 시도: change number를 string,deque 대신 정수 계산.
"""


from collections import deque
import sys
input = sys.stdin.readline

numbers= list(range(10000))
distance = [-1] * 10000
previous = list(range(10000))

def pad(string):
    return "0" * (4-len(string))+  string

#Candidate들을 담음

def change(number):
    result_dict = {}
    #Option 1 : D
    double_result = (number * 2) %10000

    result_dict["D"] = double_result
    
    #option 2 : S    
    substract_result = number-1 if number else 9999
    result_dict["S"] = substract_result
    
    #option 3 : Left Rotation
    left_result = 10* (number%1000) + (number//1000)
    result_dict["L"] = left_result
    
    #Option 4: right rotation
    right_result = (number%10) * 1000 + (number//10)
    result_dict["R"] = right_result
    
    return result_dict
    
def bfs(start, end, distance_q, previous):
    """
    @params start : 시작하는 point
    @params end   : 끝나는   point
    @params distance_q : 시작점에서의 거리를 담을 큐로, -1로 초기화
    @params previous   : 이전 탐색 지점과 옵션을 담을 큐
    """
    
    #Memory 초기화
    distance_q = distance_q[:]
    
    #시작점은 거리가 0, 이전 탐색지점은 없음
    distance_q[start] = 0
    previous[start] = (start, "")
    
    #BFS 시작
    q = deque([start])
    
    DSLR_order=[]
    while q:
        now = q.popleft()
        
        
        #Loop 종료 조건
        if now == end : 
            break
            
        #BFS 시작
        candidates = change(now)
        for change_option, candidate in candidates.items():
            if distance_q[candidate] >=0 : 
                continue #이미 방문
            else:
                distance_q[candidate] = distance_q[now] + 1
                previous[candidate] = (now, change_option)
                q.append(candidate)
                
    # 명령어 배열 출력
    
    current = end
    while current!= start:
        prev,option = previous[current]
        DSLR_order.append(option)
        current = prev
    DSLR = "".join(DSLR_order[::-1])      
    return DSLR
        

if __name__ == "__main__":

    T = int(input().rstrip())

    for _ in range(T):
        start, end = map(int,input().rstrip().split())
        print(bfs(start, end, distance, previous))
