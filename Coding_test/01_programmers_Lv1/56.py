# 신고 결과 받기

from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)

    user_list_who_i_report = defaultdict(set)
    num_of_reported = defaultdict(int)
    suspended = []

    for r in report:
        do_report, be_reported = r.split()

        num_of_reported[be_reported] += 1
        user_list_who_i_report[do_report].add(be_reported)

        if num_of_reported[be_reported] == k:
            suspended.append(be_reported)

    for s in suspended:
        for i in range(len(id_list)):
            if s in user_list_who_i_report[id_list[i]]:
                answer[i] += 1

    return answer

# def solution(id_list, report, k):
#     answer = [0]*len(id_list)
#     final_answer = [0]*len(id_list)
#     report = list(set(report))

#     for i in range(len(report)):
#         x = report[i].split(' ')
#         for j in range(len(id_list)):
#             if id_list[j] == x[1]:
#                 answer[j] += 1

#     for m in range(len(report)):
#         x = report[m].split(' ')
#         for n in range(len(id_list)):
#             if k <= answer[n] and x[1] == id_list[n]:
#                 y = id_list.index(x[0])
#                 final_answer[y] += 1

#     return final_answer