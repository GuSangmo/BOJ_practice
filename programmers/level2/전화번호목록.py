"""
Progarmmers Lv2. 

전화번호 목록
"""

"""
60 minutes. 

문제 똑바로 읽기.

"""


from collections import defaultdict

def solution(phone_book):
    #접두어의 정의 : 크기 순으로 정렬하여, 맨 앞에서 겹치는지만 체크하면 충분하다.
    #기존 것들의 크기에 대해 비교해야하지만, 신규 비교 대상엔 자신만 추가해야한다.
    
    cnt_dict = defaultdict(int)
    phone_book.sort(key = len)
    lengths = set()
    
    for phone_idx, phone in enumerate(phone_book):
        lengths.add(len(phone))
        windows = [phone[:size] for size in list(lengths)]
        for window in windows:
            if cnt_dict[window] > 0: 
                return False
            
            if len(window) == len(phone):
                cnt_dict[window] +=1
    return True