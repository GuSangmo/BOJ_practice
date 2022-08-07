"""
Progarmmers Lv2. 

숫자의 표현
"""

"""
10 minute. Sliding window 방식이 인상깊었음. 
처음엔 투포인터로 했으나 포기했음.
"""


def solution(n):
    #Use sliding window
    MAX = 5_00_1
    arr = list(range(1,10005))
    def window(size):
        match = 0
        start = 0 ; end = size
        win_sum = sum(arr[start:end])
        
        while end  < len(arr):
            if win_sum == n : 
                match+=1
                #print("sub_arr:", arr[start:end])
                break
            elif win_sum < n:
                win_sum = win_sum - arr[start] + arr[end]
                start +=1 
                end+=1
            else:
                break
        return match
    
    answer = 0
    for size in range(1, 151):
        answer += window(size)    
    return answer