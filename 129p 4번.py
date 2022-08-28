exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = []
for 점수 in exam:
    증가된점수 = 점수 + 5
    if 증가된점수 > 100:
        증가된점수 = 100
    score.append(증가된점수)
print(f"{score}")

"""
1.for 문을 이용한 iteration
for 점수 in exam:
    print(점수)
2.while 문을 이용한 iteration
idx = 0
while idx < len(exam):
    print(exam[idx])
    idx += 1

score = []
for 점수 in exam:
    score.append(점수 + 5)
for 점수 in range
"""