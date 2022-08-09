"""
프로그래머스 lv3 . 베스트앨범
"""

from collections import defaultdict
"""
장르 -> play 순 -> 고유번호순 
그러면, 장르별 dict를 만든 후 
play순, 고유번호순으로 정렬하자 되겠네
"""

def solution(genres, plays):
    genre_dict = defaultdict(list)
    genre_cnt = defaultdict(int)
    for idx, (genre, play) in enumerate(zip(genres,plays)):
        genre_cnt[genre] += play
        genre_dict[genre].append((play,idx))
    
    #장르별 정렬
    genres_by_plays = sorted(genre_cnt.items(), key = lambda x: -x[1])
    
    results = []
    for genre, _ in genres_by_plays:
        current_plays = genre_dict[genre]
        current_plays.sort(key = lambda x: (-x[0],x[1]))
        
        current_result = []
        if len(current_plays) < 2:
            current_result = [current_plays[0][1]]
        else:
            current_result = [current_plays[0][1], current_plays[1][1]]
        results += current_result
    
    answer = results
    return answer