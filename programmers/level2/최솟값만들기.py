"""
Progarmmers Lv2. 

재배열 부등식
"""

"""
그리디. 최소와 최대를 섞어서 해주면 된다.
"""


def solution(A,B):
    # 재배열
    answer = sum([i *j for i,j in zip(sorted(A), sorted(B, reverse = True))])    
    return answer