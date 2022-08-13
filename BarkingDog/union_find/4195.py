#4195. 친구 네트워크
from collections import defaultdict , Counter
import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100_000)
T = int(input().rstrip())

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a,b, friend_net):
    root1 = find_parent(parent, a)
    root2 = find_parent(parent, b)
    if root1 < root2: 
        parent[root2] = root1 
        friend_net[root1] += friend_net[root2]
        print(friend_net[root1])
    elif root1 > root2: 
        parent[root1] = root2 
        friend_net[root2] += friend_net[root1]
        print(friend_net[root2])
    else:
        print(friend_net[root1])

for _ in range(T):
    F = int(input().rstrip())
    parent = defaultdict(str)
    friend_network = defaultdict(lambda : 1)
    persons = set()
    relationships = []
    for _ in range(F):
        person1, person2 = input().rstrip().split()
        relationships.append((person1, person2))
        persons.add(person1)
        persons.add(person2)
    
    #모든 사람에 대해 초기화
    for person in persons:
        parent[person] = person
    
    for person1, person2 in relationships:
        union_parent(parent, person1, person2, friend_network)
