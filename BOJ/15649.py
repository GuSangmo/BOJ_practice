#15649. N과 M(1)
"""
백트래킹 복습 시작!
"""

# Backtracking에서 중요한건 결국 상태를 어떻게 정의하는지.
import sys
input = sys.stdin.readline
N,M = map(int,input().rstrip().split())

isused = [0] * (N+1) #만들고자 하는 배열에 그 숫자가 쓰이는가
arr = [0] * M

def subseq(k,n): #k번째 원소를 배열에 추가할때
    if k == M :  #0~ (m-1)까지 추가하고, 마지막에 m되면 출력
        print(*arr, end = " ")
        print()
        return
    for i in range(1,N+1): #1~N까지 들어갈 수 있으니깐.
        if isused[i]: continue
        arr[k] = i #k번째 원소는 i로!
        isused[i] = 1
        subseq(k+1,n) 
        isused[i] = 0        
subseq(0,N)
        
