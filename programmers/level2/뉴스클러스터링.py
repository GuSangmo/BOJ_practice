
"""
프로그래머스 Lv2 -뉴스 클러스터링
"""

# 아이디어가 맘에 들었음!@

"""
20 Minute :: flood fill
"""
from collections import Counter
import math

def make_window_size2(string):
    windows = []
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            windows.append(string[i:i+2].lower())
    return windows

def solution(str1, str2):
    
    window1 = make_window_size2(str1)
    window2 = make_window_size2(str2)
    
    total_window = window1+ window2
    
    #Processing
    counter1 = Counter(window1)
    counter2 = Counter(window2)
    union_counter = {} 
    intersection_counter = {}
    for phrase in total_window:
        cnt1 =  counter1.get(phrase, 0)
        cnt2 =  counter2.get(phrase, 0)
        union_counter[phrase] = max(cnt1, cnt2)
        if min(cnt1, cnt2) > 0:
            intersection_counter[phrase] = min(cnt1, cnt2)
    
    print("union_cnt:", union_counter)
    print("intersection_cnt:", intersection_counter)
    
    if union_counter:
        answer = math.floor((sum(intersection_counter.values()) * 65536 / sum(union_counter.values())))
    else:
        answer = 65536
    return answer