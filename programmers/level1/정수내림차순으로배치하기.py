"""
Programmers lv1 - 정수내림차순으로 배치하기
"""

def solution(n):
    cands = sorted(list(map(int, list(str(n)))))[::-1]
    answer = sum([element * (10** (len(cands)-1-idx)) for idx,element in enumerate(cands)])
    return answer