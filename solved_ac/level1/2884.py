#2884. 알람 시계

H, M = map(int,input().rstrip().split())

if M < 45:
    M = 15+M
    if H> 0: H = H-1
    else: H = 23-H
else:
    M = M-45

print(H,M)