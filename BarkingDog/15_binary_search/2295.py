#2295. 세 수의 합
"""
A[i] + A[j] + A[k] = A[l]일때 l이 max가 되게끔 찾을 것!

A[i] + A[j]의 case를 새로운 배열에 집어넣을 것!

Two[m] = A[l] - A[k]

처음에 정렬할 필요가 없음
"""

def binary_search(target,arr, length):
    start = 0 ; end = length-1; 
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return 1
        elif arr[mid] >target: end = mid-1
        else: start = mid+1
    return 0


N = int(input().rstrip())
arrs = [int(input().rstrip()) for _ in range(N)]

two_set = set()
for num1 in arrs:
    for num2 in arrs:
        two_set.add(num1+num2)
two_sums = list(two_set)
M = len(two_sums)

two_sums.sort()

max_result = -1e9
for idx1 in range(N):
    for idx2 in range(N):
        target = arrs[idx1] - arrs[idx2]
        if binary_search(target, two_sums, M):
            max_result = max(max_result, arrs[idx1], arrs[idx2])
print(max_result)
        
        