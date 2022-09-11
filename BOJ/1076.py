import sys 
input = sys.stdin.readline

colors = "black brown red orange yellow green blue violet grey white".split()

color_dict = {value: (idx, 10**idx) for idx, value in enumerate(colors)}

first, second, third = eles = [color_dict[input().rstrip()] for _ in range(3)]
result = (first[0]* 10 + second[0] ) * third[1]
print(result)
