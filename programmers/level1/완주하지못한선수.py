"""
Programmers lv1 - 완주하지 못한 선수
"""

from collections import Counter
def solution(participant, completion):
    part_counter = Counter(participant)
    for people in completion:
        part_counter[people] -=1
    
    for people in part_counter:
        if part_counter[people] > 0 :
            return people