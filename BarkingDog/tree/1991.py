#1991. 트리의 순회
"""
Left/ Right 구분해서
"""

import sys 
input = sys.stdin.readline 
from collections import deque, defaultdict 

left_child = defaultdict(str)
right_child = defaultdict(str)

N = int(input().rstrip())

for _ in range(N):
    parent, l, r = input().rstrip().split()
    left_child[parent] = l 
    right_child[parent] = r

#Traverse 
def preorder(node, path):
    #Middle
    result = node

    #Left
    if left_child[node] != ".":
        result += preorder(left_child[node], path)

    #Right
    if right_child[node] != ".":
        result += preorder(right_child[node], path)        
    return result

def inorder(node, path):
    result = ""
    
    #Left
    if left_child[node] != ".":
        result += inorder(left_child[node], path)
    
    #Middle
    result +=node

    #Right
    if right_child[node] != ".":
        result += inorder(right_child[node], path)        
    return result

def postorder(node, path):
    result = ""
    
    #Left
    if left_child[node] != ".":
        result += postorder(left_child[node], path)
    
    #Right
    if right_child[node] != ".":
        result += postorder(right_child[node], path)        
    
    #Middle
    result +=node

    return result



print(preorder("A",""))
print(inorder("A",""))
print(postorder("A",""))


