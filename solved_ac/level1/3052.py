#3052. 나머지  
from collections import defaultdict

remainder_dict = defaultdict(int)
for _ in range(10):
    number = int(input().rstrip())
    remainder = number%42 
    remainder_dict[remainder] +=1 

print(len(list(remainder_dict)))