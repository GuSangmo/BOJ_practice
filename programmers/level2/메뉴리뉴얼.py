"""
Progarmmers Lv2. 메뉴 리뉴얼

30 Min.

permutations 만드는 문제
"""


"""
최대 20개. 
각 손님이 시킨 것의 원소가 2개 이상인 부분집합을 count로 세서 +1하면 충분할듯.

최대 (2^10) * 20개라 괜찮을듯..?
"""

"""
Good code:
    -most_common()을 이용하였음. 이건 개수별로 cnt시켜주므로 잘 활용하면 베리 굿!

"""



from itertools import combinations
from collections import defaultdict, Counter
def solution(orders, course):
    result = []
    for course_size in course:
        possible_order = []
        for order in orders:
            possible_order += combinations(sorted(order), course_size)
        most_ordered = Counter(possible_order).most_common()
        result += [k for (k,v) in most_ordered if v>1]
            
    return result    
    