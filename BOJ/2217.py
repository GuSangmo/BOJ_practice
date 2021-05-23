
#2217. 로프
"""
만일 K개의 로프를 사용한다고 하고, 그 K개의 로프중 
제일 힘이 약한 중량을 w라고 하자.
그러면 K개의 로프로 버틸 수 있는 최대중량은 w x K이다.

그래서 1개의 로프~N개의 로프를 사용하는 경우를 대비하여
로프를 최대중량 순으로 나열하였다.

이를 b1,........,bn이라 하면

1* b1, 2*b2,......, n* bn을 result 배열에 담아

이 중 최댓값을 반환하였다.
"""
import sys
N=int(sys.stdin.readline().rstrip())
rope_list=[int(sys.stdin.readline().rstrip()) for _ in range(N)]
sorted_rope_list=sorted(rope_list,reverse=True)
result=[(idx+1) * sorted_rope_list[idx] for idx in range(N)]
print(max(result))
