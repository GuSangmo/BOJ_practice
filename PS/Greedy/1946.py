#1946. 신입 사원
"""
결국 우리가 알고 싶은 인원의 수는
인재선발시험(standard 1)과
면접시험(standard 2)를 정렬했을때, 모순이 일어나지 않는 사람의 수를 말한다.

다시 말해,

(기준 1) 

(최저점자) -------------------> (최고점자)

가 되게끔 정렬시켜보자.

그러면 이들의 면접점수를 확인해봤을 때 , 조건을 만족하는

(기준 2)

(최고점자)<-----(최저점자)    * 몇 명은 조건에 부적합해 선발되지 못했을 것이므로

이 짧은 배열의 길이를 구하면 된다.

그를 위해, 데이터를 받은 후 정렬하고

기준 2의 데이터를 기준으로 한명씩 한명씩 조건에 맞는지를 체크하자.

"""

import sys
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    N=int(sys.stdin.readline().rstrip())
    rank_list=[]
    for _ in range(N):
        rank1,rank2=map(int,sys.stdin.readline().rstrip().split())
        rank_list.append((rank1,rank2))
    rank_list.sort()
    compare=rank_list[0][1] ; survived_ones=1
    for element in rank_list[1:]:
        if element[1]<compare: survived_ones+=1; compare=element[1]
    print(survived_ones)
