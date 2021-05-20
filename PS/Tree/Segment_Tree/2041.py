#2041. 구간 합 구하기
"""
세그먼트 트리를 공부해보기
"""

import sys
input= sys.stdin.readline


#이미 init에 구간별 정보를 다 더해놓은 것.
#이 경우는 세그먼트 트리에 구간의 합을 넣어놓은 것.
def init(start,end,node):
    if start==end:
        tree[node]= numbers[start] #numbers는 트리로 받지 않은 것
        return tree[node]
    else:
        mid=(start+end)//2
        tree[node]= init(start,mid,node*2)+ init(mid+1,end,node*2+1)
        return tree[node]  #idx를 절반으로 쪼개서 받음.

#쿼리 1: 구간합을 구하는 함수.
#Recursive하게 좌우를 쪼개서 합친다.

def get_sum(start,end,left_node,right_node, node):
    #start,end는 내가 원하는 것.
    if end<left_node or start>right_node: return 0 #안 겹침
    if left_node<=start and end<=right_node: return tree[node]
    mid=(start+end)//2
    return get_sum(start,mid,left_node,right_node,node*2)+get_sum(mid+1,end,left_node,right_node,node*2+1)
    
#쿼리 2: 특정 인덱스를 업데이트하는 함수 
def update(start,end,index,diff,node):
    if index<start or index>end: return 
    tree[node]+=diff
    
    if start!=end:
        mid=(start+end)//2
        update(start,mid,index,diff, node*2)
        update(mid+1,end,index,diff, node*2+1)

#Operation:
N,M,K=map(int,input().rstrip().split())
numbers=[]
tree= [0] * 3000000 #1200만 byte= 12MB
for _ in range(N):
    numbers.append(int(input().rstrip()))
init(0, N-1,1)

for _ in range(M+K) :
    order_type, old, new = map(int, input().rstrip().split())
    if order_type==1 :
        diff = new - numbers[old-1] #원래거랑 지금거의 차이
        numbers[old-1] = new
        update(0, N-1, old-1, diff,1)
    elif order_type== 2 :                
        print(get_sum(0, N-1 ,old-1, new-1,1))















