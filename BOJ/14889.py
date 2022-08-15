#14889. 스타트와 링크
"""
15 Minute
half_team을 만드는 경우의 수를 구성하자.
"""

import sys 
input = sys.stdin.readline
N = int(input().rstrip())
S = [list(map(int,input().rstrip().split())) for _ in range(N)]

# 최대 20만번이므로 o.k.
# 거기다가 대략 N^2 번.

visits = [False for _ in range(N)]
half = N//2
answers = []
def dfs_combinations(arr,cnt,idx):
    if cnt == half:
        answers.append(set(arr))
        return 
    for i in range(idx, N):
        if visits[i] : continue
        visits[i] = True 
        dfs_combinations(arr+[i], cnt+1,i)
        visits[i] = False 

#Execute
dfs_combinations([],0,0)


def get_arr(team):
    team_power = 0
    for ele1 in team:
        for ele2 in team:
            if ele1 == ele2: continue 
            team_power += S[ele1][ele2]
    return team_power


for i,j in zip(S, zip(*S)):
    print(i)
    print(j)



result = 1e10 

for cand_team in answers:    
    rival_team = set(list(range(N))) - cand_team
    team_ability = get_arr(cand_team)
    rival_ability = get_arr(rival_team)
    result = min(abs(team_ability- rival_ability), result)
print(result)