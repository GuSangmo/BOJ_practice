#14888. 연산자 끼워넣기
"""
연산자 count를  함수의 인자로 놓고, dfs로 앞으로 넘겨가면서 결과를 저장하자.

4 ** 10이라 뭘 하든 가능함(대략 100만)
"""

import sys 
input = sys.stdin.readline
N = int(input().rstrip())
numbers = list(map(int,input().rstrip().split()))
total_add, total_sub, total_mul, total_div = map(int,input().rstrip().split())


maximum = -1e10
minimum = 1e10

def dfs(result, index, add, sub, mul, div):
    global maximum, minimum
    if index == N-1 : 
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return result
    
    if add > 0 :
        dfs(result + numbers[index+1], index+1, add-1, sub, mul, div)
    if sub > 0 :
        dfs(result - numbers[index+1], index+1,add, sub-1, mul, div)
    if mul > 0 :
        dfs(result * numbers[index+1], index+1, add, sub, mul-1, div)
    if div > 0 :
        if result < 0 :
            next_ele = -(-result // numbers[index+1])
        else:
            next_ele = result // numbers[index+1]
        dfs(next_ele, index+1, add, sub, mul, div-1)

#Execute 
dfs(numbers[0],0,total_add,total_sub,total_mul,total_div)

print(maximum)
print(minimum)

