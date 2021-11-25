#2493. 탑 
"""
cur_max와 tower_stack을 만들어서,
tower_stack엔 각 레이저의 수신tower의 idx와 높이를 저장한다.


최대값 나오면 스택 초기화 시켜줘야함.
"""

import sys
input = sys.stdin.readline
N = int(input().rstrip())

towers = list(map(int,input().rstrip().split()))


# 5 4 6 2 3 이 0 1 0 3 3이 나와야 하는데 내 건 0 1 0 2 2가 나옴.
laser_receivers=[]
stack = []

argmax, max_height = 1, -1 

for idx, tower in enumerate(towers,1):
    flag = False
    if idx==1:
        laser_receivers.append(0)
        max_height = tower
    else:
        if tower > max_height :
            argmax  = idx   #그 근방에선 가장 큰 것!
            max_height = tower 
            stack = []
            laser_receivers.append(0) #제일 큰거니깐
        else:
            if not stack: #local max말고는 이길 놈이 없다는 거지 
                laser_receivers.append(argmax)
                stack.append((idx, tower))
            else: 
                #이미 data가 있는것이므로 하나씩 pop해가면서 비교
                while stack and not flag:
                    last_idx, last_height = stack[-1]
                    if last_height >= tower:
                        laser_receivers.append(last_idx)
                        stack.append((idx,tower))
                        flag = True
                        break
                    else:
                        stack.pop()
                        if not stack: #얘가 최대
                            stack.append((idx,tower))
                            laser_receivers.append(argmax)
                            break       
print(*laser_receivers,end=" ")
    





