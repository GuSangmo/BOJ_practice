#20040. 사이클 게임
"""
유니온 파인드를 진행하면서 cycle_check를 하고 
사이클이 있으면 0 출력
"""
import sys 
input= sys.stdin.readline 
sys.setrecursionlimit(500_000)
N, M = map(int,input().rstrip().split())
parents = list(range(N))

def find_parent(a):
    if parents[a] != a: 
        parents[a] = find_parent(parents[a])
    return parents[a]

def union_parent(a,b):
    """
    경로 압축을 통해 유니온 하는 과정에서, root가 이미 같은게 들어오면 사이클이 있다고 판단할 수 있다.
    """
    root1 = find_parent(a)
    root2 = find_parent(b)
    if root1 < root2:
        parents[root2] = root1 
        return True
    elif root1 > root2:
        parents[root1] = root2
        return True 
    else:
        return False
    
flag = False
for order in range(M):
    city1, city2 = map(int,input().rstrip().split())
    if not union_parent(city1, city2):
        flag = True
        print(order+1)
        break
    
if not flag:
    print(0)