def get_average(marks):
    평균 = float(sum(marks.values()) / len(marks.values()))
    return 평균


marks ={'국어' : 90, '영어': 80, '수학': 85}
average = get_average(marks)
print(f"평균은{average}점입니다.")

"""
for
sum = 0
cnt = 0
for k in marks:
    sum = sum + marks[k]
    cnt
"""