############################
# Level 1. 신고 결과 받기###
############################

# Time : 10 min

"""
- 여러 번 신고 가능하나, 동일 유저 신고 횟수는 1회 처리
- 그러면 유저 ID별 신고한 ID와 신고횟수를 저장하는 dict를 선언하자.
- report_list로 이중반복문을 쓰면 무조건 TLE.
"""


from collections import defaultdict
report_id_dict = defaultdict(list)
count_dict = defaultdict(int) 

def solution(id_list, report, k):
    
    #To remove duplicates
    report = list(set(report))
    for report_case in report:
        report_from, report_to = report_case.split()
        report_id_dict[report_from].append(report_to)
        count_dict[report_to] +=1
        
    mails = set()
    for user in list(count_dict):
        if count_dict[user] >= k:
            mails.add(user)
            
    answer = []
    for id in id_list:
        reported = list(report_id_dict[id])
        cnt = 0
        for reported_user in reported:
            if reported_user in mails: 
                cnt+=1
        answer.append(cnt)
    
    return answer