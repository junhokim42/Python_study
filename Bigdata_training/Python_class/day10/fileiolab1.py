import os

if os.path.exists("study.txt") :
    f = open("study.txt", "a", encoding="UTF-8")
    line = 0
    language_list = ['Python', 'HTML', 'CSS', 'JavaScript', 'R']
    while(line < 5):
        f.write(language_list[line])
        f.write('\n')
        line += 1
    f.close()
else :
    f = open("study.txt", "wt", encoding="UTF-8")
    line = 0
    language_list = ['Python', 'HTML', 'CSS', 'JavaScript', 'R']
    while(line < 5):
        f.write(language_list[line])
        f.write('\n')
        line += 1
    f.close()
