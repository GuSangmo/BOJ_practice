# 2437. 저울
"""
나코테와 유사한 문제

만들수있는지 아닌지를 비교하고자하는 수를 target이라 하자

1~N-1번째 저울로 1부터 K까지 만들 수 있다고 하면 
N번째 저울은 weight[N]+1 ~weight[N]+k까지 가능할 것이므로 다음 target은 K+1+weight[N]
이 된다. 

따라서 target=1을 기준으로, iterative하게 element들을 더해가며 target을 올리면 된다.

"""
import sys
N=int(sys.stdin.readline().rstrip())
scale_list=list(map(int,sys.stdin.readline().rstrip().split()))
scale_list.sort()

target=1; summation=0
for element in scale_list:
    if element<=target: target+=element
    else: break
print(target)