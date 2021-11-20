#10655 : 마라톤 1
"""
USACO 2014 December Prob 1

O(N^2) is impossible. Use Partial Sum instead.
"""

import sys
input= sys.stdin.readline

#Define manhatten distance
def get_dist(prev, after):
    x1, y1 = prev
    x2, y2 = after
    dist = abs(x1-x2)+ abs(y1-y2)
    return dist

N = int(input().rstrip())
coordinates = [(-1,-1) for _ in range(N)]
psum = [0]
dpsum = [0] 

dist_sum = 0 ; dist2_sum = 0 ; minimum =  int(1e10)

for case in range(N):
    curr_node = list(map(int,input().rstrip().split()))
    coordinates[case] = curr_node

for case in range(N-1):    
    curr_node = coordinates[case]  ;  next_node = coordinates[case+1]
    dist_sum += get_dist(curr_node, next_node)
    psum.append(dist_sum)
    
    if case>N-3: continue
    next2_node = coordinates[case+2]
    dist2_sum += get_dist(curr_node, next2_node)
    dpsum.append(dist2_sum)

#Minimum check 
for i in range(1,N-1):
    candidate = (dpsum[i] - dpsum[i-1])-(psum[i+1]-psum[i-1])
    if candidate<= minimum : minimum = candidate
answer = dist_sum + minimum
print(answer)