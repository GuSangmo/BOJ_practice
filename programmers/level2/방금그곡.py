"""
Progarmmers Lv2. 캐시

LRU 알고리즘을 알아야 했던 문제.

굳이 정렬시킬 필요 없이, 제거하고 바로 삭제하면 충분했다.

다른 사람은 maxlen 을 이용했음.

maxlen 이용시 추가한 것만 남는다.
"""



# LRU : 사용되었으면 캐시값을 늘리고, 아니면 이전 거 제외하고 새롭게
from collections import deque

def solution(cacheSize, cities):
    cache = {}
    total_time = 0
    for time, city in enumerate(cities):
        #Cache Hit
        if cache.get(city.lower(), -1) > -1:
            total_time +=1
            cache[city.lower()] = time

        #Cache miss    
        else:
            total_time +=5
            if len(cache.keys()) < cacheSize:
                cache[city.lower()] = time
            else:
                new_keys = sorted(cache.keys(), key = lambda x: cache[x])
                cache = {x:cache[x] for x in new_keys}
                for key in list(cache.keys()):
                    del cache[key]
                    break

                if cacheSize > 0 :
                    cache[city.lower()] = time


    answer = total_time
    return answer
