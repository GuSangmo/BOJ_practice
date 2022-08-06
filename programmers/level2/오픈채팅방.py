"""
Programmers Lv 2. 오픈채팅방
"""




# 13 minute

"""
닉네임 변경을 잘 관리해야함.

uid - nickname을 잘 mapping해야함.

query_type을 잘 관리해야겠다.

최종출력할때는 user-id의 nickname을 이용하자.
"""

from collections import defaultdict
query_dict = defaultdict(list)
in_chatroom = defaultdict(bool)
nickname_dict = defaultdict(str)
records = []
def solution(record):
    for query in record:
        if len(query.split()) ==2:
            #Exit 명령
            cmd, user_id = query.split()
            records.append([cmd,user_id])
            in_chatroom[user_id] = False

        else:
            cmd, user_id, nickname = query.split()
            nickname_dict[user_id] = nickname
            
            if cmd == "Enter":
                #Initialize
                in_chatroom[user_id] = True
                records.append([cmd, user_id])
                
            elif cmd == "Change":
                nickname_dict[user_id] = nickname
                
    final_records = []
    for cmd, user_id in records:
        if cmd == "Enter":
            query_string = f"{nickname_dict[user_id]}님이 들어왔습니다."
            final_records.append(query_string)
        elif cmd == "Leave":
            query_string = f"{nickname_dict[user_id]}님이 나갔습니다."
            final_records.append(query_string)
    
    return final_records