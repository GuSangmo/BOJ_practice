N = int(input())
for _ in range(N):
    marks = list(input().rstrip())
    sequential = 0
    total_score = 0
    for mark in marks:
        if mark == "O":
            sequential +=1 
        else:
            sequential = 0
        total_score += sequential
    print(total_score)
            
        
        
    