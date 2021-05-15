#2217. 로프
"""
정렬시킨 후 iterative하게 min값을 찾아서 계산. 
"""
import sys
N=int(sys.stdin.readline().rstrip())
rope_list=[int(sys.stdin.readline().rstrip()) for _ in range(N)]
sorted_rope_list=sorted(rope_list,reverse=True)
result=[(idx+1) * sorted_rope_list[idx] for idx in range(N)]
print(max(result))