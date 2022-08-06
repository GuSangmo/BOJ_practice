#1157. 단어 공부
"""
대소문자 중 제일 많이 사용된 알파벳
여러 개면 "?" 출력
"""

from collections import defaultdict, Counter
cnt_dict= defaultdict(int)
result_dict = defaultdict(list)

words = input().rstrip().lower()
for letter in words:
    cnt_dict[letter] +=1 

for letter, cnt in cnt_dict.items():
    result_dict[cnt].append(letter)

result_dict = sorted(result_dict.items(), key = lambda x: x[0])[::-1]

if len(result_dict[0][1])< 2: 
    print(result_dict[0][1][0].upper())
else:
    print("?")

