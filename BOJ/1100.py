#1100. 하얀 칸
cnt = 0
for row in range(8):
    input_list = list(input().rstrip())
    for col, value in enumerate(input_list):
        if value == "F":
            if row%2 == col%2:
                cnt+=1
print(cnt)