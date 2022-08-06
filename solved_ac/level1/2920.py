#2920. 음계
"""
1~ 8 과 같은지 아닌지 확인
"""

ascend = list(range(1,9))
descend = ascend[::-1]

nums = list(map(int,input().rstrip().split()))

if nums == ascend:
    print("ascending")
elif nums == descend:
    print("descending")
else:
    print("mixed")

