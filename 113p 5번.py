#for 문
"""
for 십의자리 in range(0,10):
    for 일의자리 in range(1,11):
        print(f"{십의자리 * 10 + 일의자리}", end = '\t')
    print("")
"""
#while True문(미완성)
"""
숫자 = 1
while True:
    print(f"{숫자}", end = '\t')
    if 숫자 % 10 == 0:
        print()
        숫자 += 1
        if 숫자 == 101:
            break

"""
#while 조건문
"""
숫자 = 1
while 숫자 <=100:
    print(f"{숫자}", end = '\t')
    if 숫자 % 10 == 0:
        print()
    숫자 += 1
"""