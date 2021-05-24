#12904. A와 B
"""
S->T를 만드는 연산은 여러가지로 가지치기가 되고 
이는 브루트포스로 해석될 수 있다.
그러나 두 개의 연산은 상호 배타적이기 때문에,
T의 마지막 문자열이 "A"인지 "B"인지만 확인하면 충분하다.

두 문자열의 글자 수 차이만큼 연산을 해주었다.

"""
import sys
delete_cnt=0
S=sys.stdin.readline().rstrip()
T=sys.stdin.readline().rstrip()

limit=len(T)-len(S)
while delete_cnt<limit:
    # print("current T:", T)
    if T[-1]=='B':
        T="".join(reversed(T[:-1]))
    else:
        T=T[:-1]
    delete_cnt+=1
print(int(T==S))