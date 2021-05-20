#1991. 트리 순회
"""
기초적인 트리의 순회를 구현하는 문제.

lc배열과 rc배열을 선언하면 충분한 문제이다.

이때, input이 대문자이므로 ord 아스키 값을 이용하자.

ord("A")=65임을 이용.


lc와 rc 배열을 활용해볼 수 있었던 문제.

"""

## Step 1. 트리의 left_child, right_child 배열을 만든다.
import sys
input=sys.stdin.readline
N=int(input().rstrip())
lc=[0]*(N+1)
rc=[0]*(N+1)

for _ in range(N):
    root,left,right=input().rstrip().split()
    root_idx=ord(root)-64
    if left!="." : left_idx=ord(left)-64 ; lc[root_idx]=left_idx
    if right!=".": right_idx=ord(right)-64; rc[root_idx]=right_idx
         
## Step 2. 트리 순회 타입별

#Inorder Traversal: 중위순회 : left-> node -> right 
def inorder(cur):
    if lc[cur]: inorder(lc[cur])
    print(chr(cur+64),end="")
    if rc[cur]: inorder(rc[cur])
        
#Preorder Traversal: 전위순회 : node -> left->right 
def preorder(cur):
    print(chr(cur+64),end="")
    if lc[cur]: preorder(lc[cur])
    if rc[cur]: preorder(rc[cur])
        
        
#Postorder Traversal: 후위순회 : left-> right -> node 
def postorder(cur):
    if lc[cur]: postorder(lc[cur])
    if rc[cur]: postorder(rc[cur])
    print(chr(cur+64),end="")

##Step 3. Execution 
preorder(1)
print()
inorder(1)
print()
postorder(1)





