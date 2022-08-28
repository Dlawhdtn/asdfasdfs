def vending_machine(money):
    음료수값 = 700
    음료수잔 = 0
    잔돈 = money
    print(f"음료수 = {음료수잔}개, 잔돈 = {잔돈}원")
    while True:
        if 잔돈 >= 음료수값:
            음료수잔 += 1
            잔돈 = money - 음료수잔 * 음료수값
            print(f"음료수 = {음료수잔}개, 잔돈 = {잔돈}원")
        else:
            break
vending_machine(3000)

"""
for문
def vending_machine(money):
    음료수값 = 700
    음료수최대개수 = money // 700
    for i in range(음료수최대개수+1):
        print(f"음료수 ={i}개, 잔돈 = {money-음료수값*i}원")
vending_machine(3000)
"""