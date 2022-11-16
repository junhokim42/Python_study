from random import *
score = randint(1, 100)
if score >= 90:
    print(score, '점은 A등급입니다.')
elif score >= 80:
    print(score, '점은 B등급입니다.')
elif score >= 70:
    print(score, '점은 C등급입니다.')
elif score >= 60:
    print(score, '점은 D등급입니다.')
else:
    print(score, '점은 F등급입니다.')