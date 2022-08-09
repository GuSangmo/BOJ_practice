"""
프로그래머스 lv1 . 음양 더하기

-zip 써서 풀기

"""

def solution(absolutes, signs):
    answer = sum(i * (2* int(j)-1) for i,j in zip(absolutes, signs))
    return answer