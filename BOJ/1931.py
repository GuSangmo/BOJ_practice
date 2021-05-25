#1931. 회의실 배정
"""
잘 알려진 그리디 문제.

남아있는 시간이 길수록 배정이 더 유리하다는 것은 말할 필요 없다.
"""
#Step 1. Schedule setting
import sys
input=sys.stdin.readline
N=int(input().rstrip())
meetings=[]
for _ in range(N):
    start,end=map(int,input().rstrip().split())
    meetings.append((start,end))
meetings=sorted(meetings,key=lambda x:(x[1],x[0]))

#Step 2. 정렬된 배열에 하나하나씩 시작가능여부를 체크.
meeting_cnt=0; finish_time=0
for start,end in meetings:
    if finish_time<=start:
        meeting_cnt+=1  #이전것보다 크면 갱신
        finish_time=end #새로운 끝을 갱신
print(meeting_cnt)


