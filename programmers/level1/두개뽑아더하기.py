"""
Programmers lv1 - 두개뽑아서 더하기
"""

def solution(numbers):
    answer = set()
    for idx1 in range(len(numbers)):
        for idx2 in range(idx1+1, len(numbers)):            
            answer.add(numbers[idx1]+numbers[idx2])
    answer = list(sorted(list(answer)))
    return answer