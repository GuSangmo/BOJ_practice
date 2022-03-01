#13144. List of Unique numbers
"""
start에서 end가 이미 중복이 있다면, end+1부터는 볼 필요가 없다. 
그러면, 중복이 있을때까지 end를 늘린 후, 중복이 있다면 start를 늘리면 되겠지.

중복 check = 배열 이용(약 10만 개 = 40만 byte = 0.4MB)
"""

import sys 
input = sys.stdin.readline 

N = int(input().rstrip())
duplicates = [0 for _ in range(0,100002)]
nums = list(map(int,input().rstrip().split() ))

end = 0
result_cnt = 0
for start in range(N):
    while end< N and duplicates[nums[end]]==0: #처음이라면 
        duplicates[nums[end]] +=1
        end+=1 
    #중복이 발생하지 않는 마지막 end까지의 개수 = end - start
    result_cnt += end-start        
    duplicates[nums[start]]-=1 
print(result_cnt)
