#16681. 등산
"""
max hE - D * distance.
이건 N개의 node들에 대해 각각 시도를 해봐야한다.


E가 고정된 상황이라면 사실 distance를 최소화하는게 좋다.

집-목표지 와 목표지- 고려대의 최단거리를 각각 구하면 된다.

이때, 이동거리를 무한대로 설정후, 높이 조건을 만족할때만 갱신해주자.

이 문제에서 얻을 수 있는 교훈은 다양한데, 

[1] MIN, MAX를 IMPOSSIBLE_CONDITION 으로 남발하다가 TLE
--> 조금 더 생각을 하고 코드를 짜자

[2] 다익스트라를 루프마다 하고 있었던 것.
--> 초기에 2번 실행시켜놓고 거기서 인덱싱하는게 좋다

[3] MAX,MIN의 계산
--> 이 문제를 풀때 MIN,MAX를 생각 안하고 푼게 사실이다.

"""


##STEP 1. INITIAL SETTING
import sys
import heapq
input=sys.stdin.readline
N,M,D,E=map(int,input().rstrip().split())
heights=[0]+list(map(int,input().rstrip().split()))
big_num=1e18
graph=[[] for _ in range(N+1)]
dist=[big_num]*(N+1)


for _ in range(M):
    start,end,cost=map(int,input().rstrip().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

##Step 2. 다익스트라, with constraints
def dijk(start,original_dist):
    dist=original_dist[:]
    dist[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        cur_dist,cur_node=heapq.heappop(q)
        if dist[cur_node]<cur_dist: continue #Already visited
        for near_node, near_cost in graph[cur_node]: 
            if heights[near_node]<=heights[cur_node]: continue
            candidate=dist[cur_node]+near_cost
            if dist[near_node]>candidate:
                dist[near_node]=candidate
                heapq.heappush(q,(candidate,near_node))        
    return dist
            
##Step 3 Result Execution
res1=dijk(1,dist); res2=dijk(N,dist)


if N==2: print(res1[2] if res1[2]<big_num else "Impossible")

else:
    maximum_standard=-1e18
    flag=False
    for goal in range(2,N):
        if res1[goal]<big_num and res2[goal]<big_num:
            flag=True    
        home_to_goal=res1[goal]; goal_to_univ=res2[goal]
        dist_sum= home_to_goal+goal_to_univ 
        criteria= E * heights[goal] - D * dist_sum
        maximum_standard=max(maximum_standard,criteria)
    print(maximum_standard if flag else "Impossible")


