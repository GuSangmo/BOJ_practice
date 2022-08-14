#14267. 회사 문화1 
"""
dfs를 하면서 update
"""

import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(200_000)
n, m = map(int,input().rstrip().split())
praises = [0 for _ in range(n+1)]
graphs = [[] for _ in range(n+1)]

parents = [0]+ list(map(int,input().rstrip().split()))

for idx, element in enumerate(parents):
    if idx <= 1 : continue 
    #Parent의 graph에 child를 입력
    graphs[element].append(idx)


for _  in range(m):
    praise_num, praise_cnt = map(int,input().rstrip().split())
    praises[praise_num] += praise_cnt 


#All - in -one
def dfs_all(node, praises):
    for near_node in graphs[node]:
        praises[near_node] += praises[node]
        dfs_all(near_node, praises)
dfs_all(1, praises)

for node in range(1,n+1):
    print(praises[node], end = " ")