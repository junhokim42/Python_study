# 예산
def solution(d, budget):
    answer = 0
    spend_budget = 0
    d.sort()
    print(d)
    while(spend_budget <= budget):
        if spend_budget + d[answer] <= budget:
            spend_budget += d[answer]
            answer +=1
        else:
            break
        if len(d) == answer:
            break
        
    return answer