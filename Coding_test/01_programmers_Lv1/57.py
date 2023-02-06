# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    answer = []
    # 년,월,일을 분해해서 일 단위로 통일
    y,m,d = today.split('.')
    today = int(y)*12*28 + int(m)*28 + int(d)

    # 약관 종류를 딕셔너리 형태로 바꿔줌 (약관 종류:유효기간(일 단위))
    terms = {i[:1]:int(i[2:])*28 for i in terms}

    # p : privacies 원소(수집일자)를 '일'단위로 치환
    # c : 약관종류
    for i,p in enumerate(privacies):
        y,m,d = p.split('.')
        d,c = d.split()
        p = int(y)*12*28 + int(m)*28 + int(d)
        # (수집일자 + 약관종류에 따른 일자)가 오늘을 넘지 않으면 정답(인덱스+1)에 추가
        if p+terms[c] <= today:
            answer.append(i+1)

    return answer