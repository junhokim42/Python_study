# 주차 요금 계산

import math

# fees: [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
def get_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    parking = dict()
    stack = dict()
    
    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute) # 시간 -> 분 환산

        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car] # 출차 차량 삭제
    
    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23*60+59 - minute
        except:
            stack[car] = 23*60+59 - minute
        
    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key=lambda x: x[0])]


# from math import ceil

# def to_min(t):
#     h,m=map(int, t.split(":")) #"06:00" => ["06","00"] => [06,00]
#     return h*60+m

# def solution(fees, records):
#     fee={}
#     answer = []
#     recs={}

#     for rec in records: #["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
#             t, num, io=rec.split() #05:34 5961 IN,     default : " "
#             if num in recs: #recs 딕셔너리에 키로 num이 존재한다면
#                 recs[num].append([t, io])
#             else:
#                 recs[num]=[[t,io]]

#     for rec in recs:
#             payment=fees[1]
#             total=0
#             if len(recs[rec])%2!=0: #입고는 됐는데 출고가 되지 않은 경우->출고시각:23:59
#                 recs[rec].append(['23:59', 'OUT'])
#             for r in recs[rec]: #r[0]:시각, r[1]:IN/OUT
#                 if r[1]=='IN':
#                     total-=to_min(r[0])
#                 else :
#                     total+=to_min(r[0])
#             if total > fees[0]:
#                 payment+= ceil((total-fees[0])/fees[2])*fees[3]                
#             fee[rec] = payment
    
#     for item in fee.items():
#         answer.append(item[1])
    
#     return answer