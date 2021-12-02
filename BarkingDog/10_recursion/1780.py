#1780. 종이의 개수
"""
이것도 마찬가지로, string을 파티션해서 각각을 더해주면 됌.
이때 return하는 함숫값은 array인 것으로.
"""

import sys
input=sys.stdin.readline
N=int(input().rstrip())
papers=[list(map(int,input().rstrip().split())) for _ in range(N)]
def paper_cnt(num, string):
    result=[0,0,0]
    if num==3:
        for row in string:
            for element in row:  #-1,0,1 corresponds to idx 0,1,2
                result[element+1]+=1
        if result.count(0)>=2:
            idx= result.index(9)
            result[idx]= 1 
        return result        
    else:   
        third=num//3 ; result=[0,0,0]
        intervals=[(0,third),(third,2*third),(2*third,num)]
        
        #STRING PARTITION
        for row_s,row_e in intervals:
            for col_s,col_e in intervals:
                partition=[ele[row_s:row_e] for ele in string[col_s:col_e]]
                operation=paper_cnt(third, partition)
                result=[i+j for i,j in zip(result,operation)]
        
        #SAME SUBSEQUENCE PROCESSING
        if sum(result)==9:
            if result[0]==9: return [1,0,0]
            elif result[1]==9: return [0,1,0]
            elif result[2]==9: return [0,0,1]
        return result
print(*paper_cnt(N,papers),sep="\n")
        