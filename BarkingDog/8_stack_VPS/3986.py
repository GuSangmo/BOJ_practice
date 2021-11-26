#3986. 좋은 단어
"""
A와 B를 서로 매칭시키면서 궤가 맞아 떨어지는지 확인. 
VPS 문제와 동일

top과 이번 원소가 같을때 pop시키고, 그 외엔 stack에 append!

"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
good_words = 0
for _ in range(N):
    words = list(input().rstrip())
    stack = []
    #결국 A,B는 짝수개씩 매칭이 되어야하므로, 
    #매칭되면 pop 2번해주기!
    #홀짝성을 판별하는 parity변수 선언

    for word in words:
        if not stack : 
            stack.append(word)
            continue
        if word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)
    if not stack: good_words+=1 
print(good_words)
        