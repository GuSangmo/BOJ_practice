
"""
프로그래머스 Lv2 -튜플
"""

"""
길이 순으로 정렬한 다음에, 마지막 것부터 차집합을 시켜나가면 되지 않을까
"""
import re

def solution(s):
    pattern = s.split("},{")
    pattern[0] =  re.sub("[\}\{]","",pattern[0])
    pattern[-1] =  re.sub("[\}\{]","",pattern[-1])
    
    processed = []
    for per_pattern in pattern:
        processed.append(set(map(int, per_pattern.split(","))))
    processed.sort(key = len)
    
    tuples = []
    previous = set()
    
    for element in processed:
        minus = element.difference(previous)
        tuples.append(list(minus)[0])
        previous = element
    return tuples
    
