입력 = int(input("초를 입력하세요:"))
시간 = 입력 // 3600
분 = 입력 % 3600 // 입력
초 = 입력 % 60
print(f"변환 결과는 {시간}시간 {분}분 {초}초입니다.")

"""
입력 = int(input("초를 입력하세요:"))
시간 = 입력 // 3600
분 = 입력 // 60
    if 분 >= 60;
    분 = 분 % 60
초 = 입력 % 60
print(f"변환 결과는 {시간}시간{분}분{초}초입니다.")
"""