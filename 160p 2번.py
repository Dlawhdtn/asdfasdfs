exam = []
print("점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.")
while True:
    점수 = int(input("점수입력:"))
    if 점수 < 0:
        break
    exam.append(점수)
최대 = max(exam)
최소 = min(exam)
평균 = sum(exam) / len(exam)
print(f"평균 = {평균}, 최대 = {최대}, 최소 = {최소}")

"""
내장함수를 쓰지않고 풀어보기
"""
