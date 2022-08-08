"""
Progarmmers Lv2. 주차요금계산

단순 구현 문제인데, 상태 update하는게 생각보다 귀찮았다.
"""


"""
22 minute
"""
import math
from collections import defaultdict

#마지막 주차 빼는 용도
end_time = 60 * 23 + 59

def calculate_log(logs):
    #모든 log는 짝수개
    time = 0
    for idx in range(len(logs))[::2]:
        in_log, out_log = logs[idx] , logs[idx+1]
        time += (out_log[0] - in_log[0])
    return time

def calculate_fee(time, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees
    if time <= basic_time:
        return basic_fee
    else:
        total_fee = basic_fee + math.ceil((time  -  basic_time) / unit_time) * unit_fee 
        return total_fee

def solution(fees, records):       
    record_dict = defaultdict(list)
    for record in records:
        time, number, status = record.split()
        hour_to_min = 60 * int(time.split(":")[0])  + int(time.split(":")[1])
        record_dict[number].append((hour_to_min, status))
    
    #마지막 기준으로 "IN"된 건 23:59의 log를 추가
    result = []    
    for number in record_dict:
        last_log = record_dict[number][-1]
        if last_log[-1] == "IN":
            record_dict[number].append((end_time, "OUT"))
        
        car_time = calculate_log(list(record_dict[number]))
        car_fee = calculate_fee(car_time, fees)
        result.append((car_fee, number))
    
    result.sort(key = lambda x: int(x[1]))    
    answer = [fee for (fee,_) in result]
    return answer