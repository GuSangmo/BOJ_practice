#2268. 최솟값과 최댓값
"""
세그먼트 트리를 공부해보기.

이번엔 최솟값과 최댓값이다.


최댓값을 찾을때는 초기값을 0으로 설정하는게 타당하다.
갈수록 업데이트 될 것이므로.


init은 잘됐는데 get_min이 뭔가 이상한것같음

네이밍만 고쳤는데 된걸 보면, init2나 init 등 변수 네이밍을 이상하게 해서 
코드가 스파게티가 되었던것같음.

네이밍은 신중하게 하자. 


"""

import sys
input= sys.stdin.readline
big_num=1000000007

#구간별 최댓값을 담을 트리
def max_init(start,end,node):
    if start==end:
        max_tree[node]= numbers[start] #numbers는 트리로 받지 않은 것
        return max_tree[node]
    else:
        mid=(start+end)//2
        max_tree[node]= max(  max_init(start,mid,node*2),   max_init(mid+1,end,node*2+1) )
        return max_tree[node]  #idx를 절반으로 쪼개서 받음.

    
#구간별 최솟값을 담을 트리
def min_init(start,end,node):
    if start==end:
        min_tree[node]= numbers[start] #numbers는 트리로 받지 않은 것
        return min_tree[node]
    else:
        mid=(start+end)//2
        min_tree[node]= min(  min_init(start,mid,node*2),   min_init(mid+1,end,node*2+1) )
        return min_tree[node]  #idx를 절반으로 쪼개서 받음.
    
    
#쿼리 1: 구간합을 구하는 함수.
#Recursive하게 좌우를 쪼개서 합친다.

def get_max(start,end,left_node,right_node, node):
    #start,end는 내가 원하는 것.
    if end<left_node or start>right_node: return 0 #안 겹침
    if left_node<=start and end<=right_node: return max_tree[node]
    mid=(start+end)//2
    return max(  get_max(start,mid,left_node,right_node,node*2),  get_max(mid+1,end,left_node,right_node,node*2+1)  )

def get_min(start,end,left_node,right_node, node):
    #start,end는 내가 원하는 것.
    if end<left_node or start>right_node: return 3e9 #안 겹침
    if left_node<=start and end<=right_node: return min_tree[node]
    mid=(start+end)//2
    return min(  get_min(start,mid,left_node,right_node,node*2),  get_min(mid+1,end,left_node,right_node,node*2+1)  )





#쿼리 2: 특정 인덱스를 업데이트하는 함수 
# def update(start,end,index,diff,node):
#     if index<start or index>end: return
#     tree[node]+=diff
#     if start!=end:
#         mid=(start+end)//2
#         update(start,mid,index,diff, node*2)
#         update(mid+1,end,index,diff, node*2+1)

#Operation:
N,M=map(int,input().rstrip().split())
numbers=[]
max_tree= [0] * 300000
min_tree=[1e9] * 300000 #어차피 min을 찾아야하잖아요


#데이터 입력받기
for _ in range(N):
    numbers.append(int(input().rstrip()))

max_init(0, N-1,1)
min_init(0,N-1,1)
    
for _ in range(M) :
    idx1, idx2 = map(int, input().rstrip().split())
    res1=get_min(0,N-1,idx1-1,idx2-1,1)
    res2=get_max(0,N-1 ,idx1-1, idx2-1,1)
    print(res1, res2)