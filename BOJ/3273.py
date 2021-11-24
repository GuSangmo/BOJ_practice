
#3273: 두 수의 합

"""

ai+aj = x를 만족하는 쌍의 수를 구하기

ai <=1000000이니 괜찮을 듯. 128MB = 3200만개까지 가능

Initial code : i<j 를 고려하지 못했음.

ex) 2, 1, 2에서 가운데를 2번 인식함.

2nd code :  exist[num], exist[X-num]을 이용할 시 
X-num이 2 * BIG_NUM까지 갈 수 있어,
exist를 더 크게 선언해야 했음.

"""

BIG_NUM = int(1e6)
import sys
input= sys.stdin.readline

exist = [0] * (2 * BIG_NUM+1)
N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
X = int(input().rstrip())
pair = 0
for num in nums:
    exist[num] +=1
    if X>num and exist[X - num] :
        if num * 2 == X: continue #이 경우는 제외        
        pair += 1 
print(pair)

