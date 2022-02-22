#1654. 랜선 자르기
"""
parameteric search.

- sum of (stick //length) >= N이 나오게 하는 length 중 최대인 걸 찾기

"""

import sys 
input = sys.stdin.readline 

K,N = map(int,input().rstrip().split())

#sticks : K개의 막대기
sticks = []
max_stick = -1e8
for _ in range(K):
    element = int(input().rstrip())
    max_stick = max(max_stick,element)
    sticks.append(element)


#O(N)
def check(arr,length):  
    result = 0
    for element in arr:
        result += (element//length)
    return result


def operation(arr):
    start = 1
    end   = max_stick
    while start+1 < end:
        mid = (start + end)//2
        if check(arr,mid)>=N: start = mid 
        else: end = mid
    
    if check(arr,end)>=N: return end
    else: return start
        
result = operation(sticks)
print(result)
    
    
