#1717. 집합의 표현
"""
유니온 파인드 연습
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M = map(int,input().rstrip().split())

parent = [i for i in range(N+1)]
#경로 압축
def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a,b):
    root1 = find_parent(a)
    root2 = find_parent(b)
    if root1 < root2:
        parent[root2] = root1
    elif root1 > root2:
        parent[root1] = root2

for _ in range(M):
    cmd, a, b = map(int,input().rstrip().split())
    if cmd == 1 :
        if find_parent(a) != find_parent(b):
            print("NO")
        else:
            print("YES")
    else:
        union_parent(a,b)

