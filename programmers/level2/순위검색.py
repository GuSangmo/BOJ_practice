"""
Progarmmers Lv2. 순위검색

좋은 문제! 효율성을 따져봤어야 했다.
10억개나 되서 그렇구나.

이분탐색을 쓰면 해결된다.

__
좋은 풀이 중에서, "-"도 애초에 넣는 방법이 있었다. 참고하자.

"""

from collections import defaultdict
from itertools import product
from bisect import bisect_left, bisect_right
def solution(info, query):
    answer = []

    number = defaultdict(list)
    for information in info:
        pl, position, expert, soul_food, score = information.split()
        number[(pl,position,expert,soul_food)].append(int(score))

    for key in number.keys():
        number[key].sort()

    for per_query in query:
        conditions = [string for string in per_query.split() if string != "and"]
        result_conditions = []
        for idx, condition in enumerate(conditions):
            if idx == len(conditions)-1:
                query_score = int(condition)
                break

            if condition == "-":
                if idx == 0 : result_conditions.append(["cpp", "java", "python"])
                elif idx== 1: result_conditions.append(["frontend", "backend"])
                elif idx== 2: result_conditions.append(["junior", "senior"])
                elif idx== 3: result_conditions.append(["chicken", "pizza"])
            else:
                result_conditions.append([condition])
        value = 0
        for pair in product(*result_conditions):
            pos1 = bisect_left(number[pair], query_score)
            value += len(number[pair]) - pos1

        answer.append(value)


    return answer
