# 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    
    list_n = [i for i in range(1, n+1) if n%i == 0]
    list_m = [j for j in range(1, m+1) if m%j == 0]
    
    gcd = max(list(set(list_n).intersection(list_m)))
    lcm = n*m//gcd
    answer.append(gcd)
    answer.append(lcm)
    
    return answer