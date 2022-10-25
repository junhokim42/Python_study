# 2016년

import datetime

def solution(a, b):
    answer = ''
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    
    answer = day[datetime.date(2016,int('{}'.format(a)),int('{}'.format(b))).weekday()]
    
    return answer