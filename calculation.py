"""
dfs로 타겟 만드는 방법 찾는 문제
"""


def solution(number, target):
    """
    whether plus, minus, just keep the limit
    """
    max_length = len(number)
    answer = 0
    isvisit = [False ] * max_length
    def dfs(cnt, summation, idx):
        nonlocal answer
        if idx == max_length:
            if summation == target: 
                answer +=1 
            return
        dfs(cnt+1, summation + number[idx], idx+1)
        dfs(cnt+1, summation - number[idx], idx+1)
        
    dfs(0,0,0)
    return answer

num1 = [1,1,1,1,1]
target1 = 3 

num2 = [4,1,2,1]
target2= 4 

print("case1:", solution(num1,target1))
print("case2:", solution(num2,target2))
    
    
    
