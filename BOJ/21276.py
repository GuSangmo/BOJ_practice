#21276. 계보 복원가 호석
"""
위상정렬로 원래 출력 순서를 유지하되, 정보만 가지고 있으면 충분할듯.
(child와 descendant를 구분하기 위함)

dict에 descent 정보를 저장하자.
이번에도 역시, defaultdict가 선언되지 않은 건 key로 저장하지 않음에 유의하자.
"""

import sys 
from collections import deque , defaultdict
input = sys.stdin.readline 

N = int(input().rstrip())
graph = defaultdict(list)
indegree = defaultdict(int)

#그래프 초기화
for key in input().rstrip().split():
    graph[key] = []
    indegree[key] = 0

M = int(input().rstrip())
for _ in range(M):
    child, parent = input().rstrip().split()
    graph[parent].append(child)
    indegree[child] +=1

#위상정렬 초기 점들 설정 및 값들 출력
"""
result() 함수에, 위상정렬을 하면서 다음 번 방문에 추가되는 node들을 dict 형태로 담자
"""
def result():
    deq = deque([])
    subtree = defaultdict(list)
    for person in list(graph):
        subtree[person] = []
        if indegree[person] == 0 :
            deq.append(person)
    
    #초기값 출력
    tmp = sorted(deq)
    print(len(tmp))
    print(*tmp)

    #위상 정렬
    while deq:
        cur_node = deq.popleft()
        for near_node in graph[cur_node]:
            indegree[near_node] -= 1 
            if indegree[near_node] == 0 :
                subtree[cur_node].append(near_node)
                deq.append(near_node)
    
    #조건에 맞게 출력

    for key in sorted(subtree):
        print(key, len(subtree[key]), *sorted(subtree[key]))

    return subtree


#Execute!    
result()





