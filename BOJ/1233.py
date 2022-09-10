from itertools import combinations
from collections import defaultdict
s1, s2, s3 = map(int,input().split())

sum_dict = defaultdict(int)
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            sum_dict[i+j+k] +=1

results = sorted(sum_dict.items(), key = lambda x: (-x[1],x[0]))
print(results[0][0])