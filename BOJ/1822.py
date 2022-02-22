#1822. 차집합
"""
A : N 개
B : M 개

라고 하면 A의 원소들에 대해 binary_search를 하면 된다.

M log M(B를 정렬) + N log M 
"""

def binary_search(arr, target, length):
    start = 0 ; end = length-1 
    while start +1 < end: 
        mid = (start+end)//2
        if arr[mid] == target : return 1
        elif arr[mid]> target: end = mid-1 
        else: start = mid+1 
    if arr[start] == target or arr[end] == target : return 1 
    return 0

exclusives =  []

num_a, num_b = map(int,input().rstrip().split())

list_a = list(map(int,input().rstrip().split()))
list_b = list(map(int,input().rstrip().split()))

list_a.sort()
list_b.sort() 

for element in list_a: 
    if binary_search(list_b, element, num_b): continue
    exclusives.append(element)

if exclusives: 
    print(len(exclusives))
    print(*exclusives, sep = " ")
else:
    print(0)


