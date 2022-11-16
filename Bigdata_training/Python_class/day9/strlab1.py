from operator import indexOf


def myemail_info(p):
    if '@' not in str(p):
        return None
    else:
        p_index = p.index('@')
        tup =(p[0:p_index], p[p_index+1:len(p)])
        return tup

print(myemail_info('Bigdata@naver.com'))